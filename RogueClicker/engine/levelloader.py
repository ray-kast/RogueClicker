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
    
    self.blocks = self.getblocks()
    info = pg.display.Info()
    self.w = info.current_w
    self.h = info.current_h
    self.surf = pg.Surface([self.w,self.h])
    size = 100
    ents = []
    for block in self.blocks:
      print(np.multiply(block, size))
      ents.append(Entity(self.world, np.multiply(block, size), (0, 0), self.surf, 1, self.world.envSprites))

  def getblocks(self):
    size = 9
    blocks = []
    x = 0 
    y = 0
    while y<9:
      blocks.append(self.asurf.get_at((x, y))[0:3])
      
      if x == 8:
        y += 1
        x = 0
      else:
        x+=1
    
    print(blocks)
    block = []
    x = 0
    for i in blocks:
      
      if i == (0,0,0):
        if x/9 <1: 
          block.append(([x,1], 100))
        else:
          block.append(([(x-(9*(x//9)-1)),(x//9)], 100))
      x+=1

    print( block)
    return block

