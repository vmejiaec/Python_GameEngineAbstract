from abc import ABC, abstractmethod

class TimeManager(ABC):
    @abstractmethod
    def tick(self):
        pass