from engine.color import *
from engine.mob import *

class Player(Mob):
  def __init__(self, pos, *groups):
    Mob.__init__(self, pos, pg.image.load("assets\\sprites\\test.png"), 4, *groups)