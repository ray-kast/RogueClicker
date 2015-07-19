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
    for block in self.blocks:
      ents.append(Entity(self.world, np.multiply(block, size), (0, 0), surf, 1, self.world.envSprites))

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
    for i in blocks:
      if blocks[i] == Colors.Black:
        if i/9 < 1:
          block[i] = ([i,1], 100)
        else:
          block[i] = ([(i-(9*(i//9)-1)),(i//2)], 100)

    print( block)
    return block

