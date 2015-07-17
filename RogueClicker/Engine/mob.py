from engine.entity import *

class Mob(Entity):
  def __init__(self, pos, surf, scl, *groups):
    Entity.__init__(self, pos, surf, scl, *groups)

    self.isOnGround = False

    self.walkDir = 0
    self.isJumping = False