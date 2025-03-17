from abc import ABC, abstractmethod

'''  Renderer
  init
  clear
  display
  draw
  quit
'''

class Renderer(ABC):
    @abstractmethod
    def init(self, width: int, height: int, title: str):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def draw(self, obj):
        pass

    @abstractmethod
    def quit(self):
        pass