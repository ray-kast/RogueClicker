from engine.dummysprite import *
from engine.game import *
from engine.world import *
from engine.menu import *

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def init(self):
    Game.init(self)

    self.font = pg.font.Font("assets\\fonts\\FreePixel.ttf", 32)

    self.menu = Menu(self.win)

    norm = ((99, 98, 87), Colors.Black)
    hover = ((125, 122, 106), Colors.White)
    act = ((209, 55, 2), Colors.White)

    Menu.Button(self.menu,
                lambda btn: None,
                norm,
                hover,
                act,
                self.font,
                "Play",
                (8, 8),
                (320, 48))

    Menu.Button(self.menu,
                lambda btn: None,
                norm,
                hover,
                act,
                self.font,
                "Options",
                (8, 64),
                (320, 48))

    Menu.Button(self.menu,
                lambda btn: self.postQuit(),
                norm,
                hover,
                act,
                self.font,
                "Quit",
                (8, 120),
                (320, 48))

    self.world = World(self.win)

    self.currDrawing = self.menu

    self.dummysprite = DummySprite((10, 10), self.world.bkgdSprites)