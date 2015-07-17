from engine.entity import *

class Mob(Entity):
  def __init__(self, pos, surf, scl, *groups):
    Entity.__init__(self, pos, surf, scl, *groups)

    self.isOnGround = False

    self.walkX = 0
    self.walkY = 0
    self.isJumping = False