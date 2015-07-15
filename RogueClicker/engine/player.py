from engine.mob import *

class Player(Mob):
  def __init__(self, *groups):
    Mob.__init__(self, *groups)