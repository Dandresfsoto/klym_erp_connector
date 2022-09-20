from .base import ConnectorStrategy
from ..dataclass.connectors import SAPConnectorDataclass
from typing import Dict


class SapConnector(ConnectorStrategy):

    def get_config(self, config: Dict):
        return SAPConnectorDataclass(**config)
