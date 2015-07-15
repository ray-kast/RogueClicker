from engine.dummysprite import *
from engine.game import *
from engine.world import *
from engine.menu import *

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def init(self):
    Game.init(self)

    self.menu = Menu(self.win)

    self.world = World(self.win)

    self.currDrawing = self.menu

    self.dummysprite = DummySprite((10, 10), self.world.bkgdSprites)