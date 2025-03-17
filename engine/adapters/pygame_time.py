import pygame
from engine.interfaces.time import TimeManager
from engine.settings import FPS

class PygameTime(TimeManager):
    def __init__(self):
        self.clock = pygame.time.Clock()
    
    def tick(self):
        self.clock.tick(FPS)