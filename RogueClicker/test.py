﻿from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *

class TestGame(Game):
  def __init__(self):
    Game.__init__(self)

  def doBlocks(self, blocks, size):
    surf = pg.Surface((size, size))

    surf.fill(Colors.Black)
    
    ents = []
    
    for block in blocks:
      ents.append(Entity(self.world, np.multiply(block, size), (0, 0), surf, 1, self.world.envSprites))

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
                self.play,
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
                "  Options",
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

    self.player = Player(self.world, (110, 110), (0, 0), self.world.dynSprites)

    surf = pg.Surface((100, 100))

    surf.fill(Colors.Black)

    self.blocks = self.doBlocks([
      (1, 2),
      (2, 2),
      (3, 2),
      (4, 1)
    ], 100)

    self.currDrawing = self.menu

  def play(self, btn):
    self.win.fill(Colors.Green)

    self.currDrawing = self.world