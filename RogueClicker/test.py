from engine.dummysprite import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *

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

    rect = pg.Rect(0, 8, 320, 48)

    xc = 1
    yc = 3

    x = self.scrRect.centerx - (rect.right * xc - rect.left) / 2
    y = self.scrRect.centery - (rect.bottom * yc - rect.top) / 2

    Menu.Button(self.menu,
                lambda btn: None,
                norm,
                hover,
                act,
                self.font,
                "Play",
                (x, y),
                rect.size)

    Menu.Button(self.menu,
                lambda btn: None,
                norm,
                hover,
                act,
                self.font,
                "Options",
                (x, y + rect.bottom),
                rect.size)

    Menu.Button(self.menu,
                lambda btn: self.postQuit(),
                norm,
                hover,
                act,
                self.font,
                "Quit",
                (x, y + rect.bottom * 2),
                rect.size)

    self.world = World(self.win)

    self.player = Player([200, 200], "assets\\sprites\\test.png", self.world.dynSprites)

    self.currDrawing = self.world

    #self.dummysprite = DummySprite((10, 10), self.world.bkgdSprites)