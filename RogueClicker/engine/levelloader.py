from engine.entity import *
from engine.game import *
from engine.menu import *
from engine.player import *
from engine.world import *
from test import *

class level(Drawable):
  def __init__(self, pic):
    #i want this to be an entire screen if possible. 
    self.asurf = pg.image.load(pic)
  def getblocks(self):
    blocks = pg.image.tostring(self.asurf, "RGB")
    block = []
    for i in blocks:
      if blocks[i] == Colors.Black:
        if i/9 < 1:
          block[i] = ([i,1], 100)
        else:
          block[i] = ([(i-(9*(i//9)-1)),(i//2)], 100)  
      #if blocks[i] == Colors.CornflowerBlue:
       # blocks[i] = (Colors.CornflowerBlue, 100)
      #if blocks[i] == Colors.Green:
       # blocks[i] = (Colors.Green, 100)
      #if blocks[i] == Colors.White:
       # blocks[i] = (Colors.White, 100)
    return block



one = level()