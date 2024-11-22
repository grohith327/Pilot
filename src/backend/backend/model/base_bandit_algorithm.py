from abc import ABC, abstractmethod
from backend.element import Element


class BanditAlgorithm(ABC):
    @abstractmethod
    def get_recommendation(self) -> str:
        pass

    @abstractmethod
    def update(self, element_id: str, reward: bool):
        pass

    @abstractmethod
    def save_checkpoint(self, checkpoint_path: str):
        pass

    @abstractmethod
    def load_from_checkpoint(self, checkpoint_path: str):
        pass

    @abstractmethod
    def get_stats(self) -> dict:
        pass
