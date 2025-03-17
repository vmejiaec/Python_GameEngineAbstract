import pygame
from ..interfaces.rectInterface import RectInterface

class PygameRect(RectInterface):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x,y, width, height)

    def set_position(self, x: int, y: int):
        self.rect.x = x
        self.rect.y = y
    
    def get_position(self):
        return self.rect.x, self.rect.y
    
    def move(self, dx: int, dy: int):
        self.rect.x += dx
        self.rect.y += dy
    
