from typing import Callable, Dict, List

class EventManager:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]]={}
    
    def subscribe(self, event_type: str, callbak: Callable):
        if event_type not in self.listeners:
            self.listeners[event_type]= []
        self.listeners[event_type].append(callbak)
    
    def notify(self, even_type: str, event_data=None):
        if even_type in self.listeners:
            for callback in self.listeners[even_type]:
                callback(event_data)