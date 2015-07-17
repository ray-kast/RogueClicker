from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *
from test import *

class level():
  def __init__(self, blocks):
    self.pic = pic
  def doBlocks(self, blocks, size):
    surf = pg.Surface((size, size))

    surf.fill(Colors.Black)
    
    ents = []
    
    for block in blocks:
      ents.append(Entity(self.world, np.multiply(block, size), (0, 0), surf, 1, self.world.envSprites))