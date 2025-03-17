import pygame
from  ..interfaces.event_source import EventSource

class PygameEventSource(EventSource):
    def get_events(self):
        return pygame.event.get()