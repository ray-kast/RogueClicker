from engine.dummysprite import *
from engine.game import *
from engine.world import *

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def init(self):
    Game.init(self)

    self.world = self.currDrawing = World(self.win)

    self.dummysprite = DummySprite((10, 10), self.world.bkgdSprites)