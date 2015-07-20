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
    for block in self.blocks:
      print(block[0])
      print([((block[0][0] * block[1])),(block[0][1] * block[1])])
      
      ents.append(Entity(self.world, [(block[0][0] * block[1]),(block[0][1] * block[1])], (0, 0), self.surf, 2, self.world.envSprites))

  def getblocks(self):
    size = 16
    blocks = []
    size = self.asurf.get_rect().size

    for row in range(size[1]):
      for col in range(size[0]):
        block = self.asurf.get_at((col, row))[0:3]

        if block == (0, 0, 0):
          blocks.append(([col, row], 64))
        if block == (255, 0, 0):
          if row < (size[1] - 1) \
            and self.asurf.get_at((col, row + 1))[0:3] != (255, 0, 0):
            self.spawn = (col * 64, (row + .5) * 64) #Set spawn point
      
    print(blocks)
    return blocks

