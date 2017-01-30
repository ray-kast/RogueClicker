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

    self.surf = pg.image.load("assets/sprites/blocks/metalBlock32x32.png")

    self.size = self.surf.get_rect().size
    self.scl = 2

    self.asize = np.multiply(self.size, self.scl)

    #25x14
    ents = []
    shEnts = []
    vEnts = []

    self.shSurf = pg.Surface(self.size)
    self.shSurf.set_alpha(int(255 * .2))

    self.vSurf = pg.Surface(self.size)
    self.vSurf.fill(Colors.Green)
    self.vSurf.set_alpha(int(255 * .25))

    for block in self.blocks:
      pos = np.multiply(block[0], self.asize)
      
      if block[2] == 0:
        ents.append(StaticEntity(self.world, pos, (0, 0), self.surf, 2, self.world.envSprites))
        shEnts.append(Entity(self.world, np.add(pos, np.multiply(self.surf.get_rect().size, .25)), (0, 0), self.shSurf, 2))

      elif block[2] == 1:
        vEnts.append(Entity(self.world, pos, (0, 0), self.vSurf, 2))
        self.world.vEnts = vEnts

    self.world.bkgdSprites.add(*shEnts, layer = 2)
    self.world.bkgdSprites.add(*vEnts, layer = 1)

  def getblocks(self):
    size = 16
    blocks = []
    size = self.asurf.get_rect().size

    for row in range(size[1]):
      for col in range(size[0]):
        block = self.asurf.get_at((col, row))[0:3]

        if block == (0, 0, 0):
          blocks.append(([col, row], 64, 0))
        elif block == (255, 0, 0):
          if row < (size[1] - 1) \
            and self.asurf.get_at((col, row + 1))[0:3] != (255, 0, 0):
            self.world.playerSpawn = np.array(((col + .5) * 64, (row - .5) * 64), np.float)
        elif block == (0, 255, 0):
          blocks.append(([col, row], 64, 1))
        elif block != (255, 255, 255):
          print("Unknown color {0} at ({1}, {2})".format(block, (col, row)))
    
    return blocks
  def newlevel(self, pic, world):
    pass
