from .backends.base import ConnectorStrategy
from typing import Dict


class ErpConnector:

    def __init__(self, strategy: ConnectorStrategy, config: Dict):
        self._strategy = strategy
        self.config = self.get_config(config=config)

    @property
    def strategy(self) -> ConnectorStrategy:
        return self._strategy

    def get_config(self, config: Dict):
        return self.strategy.get_config(config=config)
