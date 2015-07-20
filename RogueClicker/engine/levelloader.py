import numpy as np
from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *
from test import *

class level():
  def __init__(self, pic, world):
    self.world = world
    #i want this to be an entire screen if possible. 
    self.asurf = pic
    self.spawn = ()
    self.blocks = self.getblocks()
    info = pg.display.Info()
    self.w = info.current_w
    self.h = info.current_h
    self.surf = pg.image.load("assets\\sprites\\blocks\\metalBlock32x32.png")
    #25x14
    ents = []
    shEnts = []

    self.shSurf = pg.Surface(self.surf.get_rect().size)

    self.shSurf.set_alpha(int(255 * .2))

    for block in self.blocks:
      pos = np.multiply(block[0], block[1])

      ents.append(StaticEntity(self.world, pos, (0, 0), self.surf, 2, self.world.envSprites))
      shEnts.append(Entity(self.world, np.add(pos, (8, 8)), (0, 0), self.shSurf, 2, self.world.bkgdSprites))

  def getblocks(self):
    size = 16
    blocks = []
    size = self.asurf.get_rect().size

    for row in range(size[1]):
      for col in range(size[0]):
        block = self.asurf.get_at((col, row))[0:3]

        if block == (0, 0, 0):
          blocks.append(([col, row], 64))
        elif block == (255, 0, 0):
          if row < (size[1] - 1) \
            and self.asurf.get_at((col, row + 1))[0:3] != (255, 0, 0):
            self.world.playerSpawn = np.array(((col + .5) * 64, (row - .5) * 64), np.float)
        elif block == (0, 255, 0):
          if row < (size[1] - 1) \
            and self.asurf.get_at((col, row + 1))[0:3] != (0, 255, 0):
            self.world.playerFinish = np.array(((col + .5) * 64, (row - .5) * 64), np.float)
        elif block != (255, 255, 255):
          print("Unknown color {0} at ({1}, {2})".format(block, (col, row)))
      
    print(blocks)
    return blocks

