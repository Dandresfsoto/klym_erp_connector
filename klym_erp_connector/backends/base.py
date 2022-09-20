from abc import ABC, abstractmethod
from typing import Dict


class ConnectorStrategy(ABC):

    @abstractmethod
    def get_config(self, config: Dict):
        pass
