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

    self.menuBtn1 = Menu.Button(self.menu,
                                lambda btn: print(btn),
                                Colors.CornflowerBlue,
                                Colors.Black,
                                "Click!",
                                (10, 10),
                                (100, 32))

    self.world = World(self.win)

    self.currDrawing = self.menu

    self.dummysprite = DummySprite((10, 10), self.world.bkgdSprites)