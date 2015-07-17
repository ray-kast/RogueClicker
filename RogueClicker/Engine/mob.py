import numpy as np
from engine.entity import *

class Mob(DynEntity):
  def __init__(self, world, pos, vel, surf, scl, *groups):
    Entity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.isOnGround = False

    self.walkDir = 0
    self.isJumping = False

  def update(self, dt):
    self.vel[0] += self.walkDir * (.5 if self.isOnGround else .01)
    self.vel[1] += -.5 if self.isJumping and self.isOnGround else 0

    DynEntity.update(self, dt)