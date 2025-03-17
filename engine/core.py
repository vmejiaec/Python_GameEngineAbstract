from .settings import *
from .interfaces.renderer import Renderer
from .interfaces.time import TimeManager
from .interfaces.event_source import EventSource
from .adapters.pygame_keymap import KEY_MAP

from .player import Player
from .event_manager import EventManager


class Game:
    def __init__(self, player: Player, renderer: Renderer , time_manager:TimeManager, eventsource: EventSource):
        self.time_manager = time_manager
        self.renderer = renderer
        self.player = player
        self.running = True
        self.event_source = eventsource
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