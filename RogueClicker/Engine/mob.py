import numpy as np
from engine.entity import *

class Mob(DynEntity):
  def __init__(self, world, pos, vel, surf, scl, *groups):
    Entity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.isOnGround = False

    self.walkDir = 0
    self.isJumping = False

  def update(self, dt):
    self.vel += np.array([self.walkDir, -1 if self.isJumping else 0]) * .1

    DynEntity.update(self, dt)