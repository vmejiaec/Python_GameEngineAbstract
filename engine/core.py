from .settings import *
from .adapters.pygame_adaper import PygameRenderer
from .adapters.pygame_rect import PygameRect
from .adapters.pygame_time import PygameTime
from .player import Player
from .event_manager import EventManager
from .adapters.pygame_event_source import PygameEventSource
from .adapters.pygame_keymap import KEY_MAP

class Game:
    def __init__(self):
        self.time_manager = PygameTime()
        self.renderer = PygameRenderer()
        self.player = Player(PygameRect(100,100,30,30),speed=5)
        self.running = True
        self.event_source = PygameEventSource()
        self.event_manager = EventManager()

        # Registrarse al evento QUIT
        self.event_manager.subscribe("QUIT", self.on_quit)
        # Registrar al player a los eventos del teclado
        self.event_manager.subscribe("KEY_EVENT", self.player.handle_event)
    
    def init(self):
        self.renderer.init(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def update(self):
        for event in self.event_source.get_events():
            if event.type == KEY_MAP["QUIT"]:
                self.event_manager.notify("QUIT")
            elif event.type in [KEY_MAP["KEYDOWN"] ,KEY_MAP["KEYUP"]]:
                self.event_manager.notify("KEY_EVENT", event)
        self.player.move()
    
    def render(self):
        self.renderer.clear()
        self.player.draw(self.renderer)
        self.renderer.display()

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
            self.time_manager.tick()

        self.renderer.quit()

    def on_quit(self):
        self.running = False