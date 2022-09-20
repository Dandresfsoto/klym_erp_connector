from dataclasses import dataclass, fields, field
from typing import List
import cryptography.fernet
import os

import validators


def validate(instance):
    for instance_field in fields(instance):
        attr = getattr(instance, instance_field.name)
        if not isinstance(attr, instance_field.type):
            raise TypeError("Field '{0.name}' is of type {1}, should be {0.type}".format(
                instance_field, type(attr))
            )


class BaseDataclass:
    crypter: cryptography.fernet.Fernet

    def encrypt_str(self, value):
        return self.crypter.encrypt(value.encode('utf-8'))

    def decrypt_str(self, value):
        return self.crypter.decrypt(value.encode('utf-8')).decode('utf-8')

    @staticmethod
    def get_crypter():
        configured_key = os.getenv("FIELD_ENCRYPTION_KEY")

        if configured_key is None:
            raise ValueError('FIELD_ENCRYPTION_KEY must be defined in envs')

        try:
            crypter = cryptography.fernet.Fernet(configured_key)
        except Exception as error:
            raise ValueError(f'FIELD_ENCRYPTION_KEY defined incorrectly: {error}')
        else:
            return crypter


@dataclass(order=True)
class SAPConnectorDataclass(BaseDataclass):
    user: str
    password: str
    open_items_endpoint: str
    open_items_metadata_endpoint: str
    suppliers_endpoint: str
    suppliers_metadata_endpoint: str
    excluded_suppliers_tax_number_list: List = field(default_factory=list)
    valid_suppliers_tax_number_list: List = field(default_factory=list)

    def validate_url_field(self, field_name):
        if not validators.url(getattr(self, field_name)):
            raise TypeError(f"'{field_name}' is not a valid URL")
        return None

    def __post_init__(self):
        validate(self)
        self.crypter = self.get_crypter()
        self.validate_url_field('open_items_endpoint')
        self.validate_url_field('open_items_metadata_endpoint')
        self.validate_url_field('suppliers_endpoint')
        self.validate_url_field('suppliers_metadata_endpoint')
        self.password = self.decrypt_str(self.password)
