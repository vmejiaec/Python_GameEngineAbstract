from .interfaces.rectInterface import RectInterface
from .adapters.pygame_keymap import KEY_MAP

class Player:
    def __init__(self, rect: RectInterface, speed):
        self.rect = rect
        self.color = (0,255,0) # Verde
        self.speed = speed
        self.velocity = [0, 0]

    def handle_event(self, event):
        if event.type == KEY_MAP["KEYDOWN"]:
            if event.key == KEY_MAP["LEFT"]:
                self.velocity[0] = -self.speed
            if event.key == KEY_MAP["RIGHT"]:
                self.velocity[0] = self.speed
            if event.key == KEY_MAP["UP"]:
                self.velocity[1] = -self.speed
            if event.key == KEY_MAP["DOWN"]:
                self.velocity[1] = self.speed
        elif event.type == KEY_MAP["KEYUP"]:
            if event.key in (KEY_MAP["LEFT"], KEY_MAP["RIGHT"]):
                self.velocity[0] = 0
            if event.key in (KEY_MAP["UP"], KEY_MAP["DOWN"]):
                self.velocity[1] = 0

    def move(self):
        self.rect.move( self.velocity[0], self.velocity[1] )

    def draw(self, renderer):
          renderer.draw({'color':self.color, 'rect': self.rect})