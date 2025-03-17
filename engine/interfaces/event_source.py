from abc import ABC, abstractmethod

class EventSource(ABC):
    @abstractmethod
    def get_events(self):
        pass