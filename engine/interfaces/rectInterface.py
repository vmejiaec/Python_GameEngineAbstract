from abc import ABC, abstractmethod

class RectInterface(ABC):
    @abstractmethod
    def set_position(self, x: int, y: int):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def move(self, dx: int, dy: int):
        pass