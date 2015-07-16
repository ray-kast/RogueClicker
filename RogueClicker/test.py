from engine.dummysprite import *
from engine.game import *
from engine.world import *
from engine.menu import *

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def init(self):
    Game.init(self)

    self.font = pg.font.Font("assets\\fonts\\uni0553.ttf", 8)

    self.menu = Menu(self.win)

    norm = ((99, 98, 87, 255), Colors.Black)
    hover = ((211, 102, 32), Colors.Black)
    act = ((166, 91, 19), Colors.Black)

    Menu.Button(self.menu,
                lambda btn: None,
                norm,
                hover,
                act,
                self.font,
                "Click!",
                (10, 10),
                (100, 32))

    Menu.Button(self.menu,
                lambda btn: None,
                norm,
                hover,
                act,
                self.font,
                "Click 2!",
                (10, 52),
                (100, 32))

    self.world = World(self.win)

    self.currDrawing = self.menu

    self.dummysprite = DummySprite((10, 10), self.world.bkgdSprites)