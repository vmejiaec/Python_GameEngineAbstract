from engine.core import Game
from engine.adapters.pygame_event_source import PygameEventSource
from engine.adapters.pygame_time import PygameTime
from engine.adapters.pygame_renderer import PygameRenderer
from engine.adapters.pygame_rect import PygameRect
from engine.player import Player

def main():
    time_manager = PygameTime()
    event_source = PygameEventSource()
    renderer = PygameRenderer()
    player = Player(PygameRect(100,100,30,30),speed=5)
    game = Game(player, renderer, time_manager, event_source)
    game.run()

if __name__ == "__main__":
    main()