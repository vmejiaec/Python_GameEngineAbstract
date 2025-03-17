import pygame
from engine.interfaces.renderer import Renderer

class PygameRenderer(Renderer):
    def __init__(self):
        self.screen = None

    def init (self, width: int, height: int, title: str):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
    
    def clear(self):
        self.screen.fill((0,0,0))

    def display(self):
        pygame.display.flip()

    def draw(self, obj):
        pygame.draw.rect(self.screen, obj['color'], obj['rect'])

    def quit(self):
        pygame.quit()
        