import numpy as np
from engine.entity import *

class Mob(Entity):
  def __init__(self, world, pos, vel, surf, scl, *groups):
    Entity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.isOnGround = False

    self.walkDir = 0
    self.isJumping = False

  def update(self, dt):
    
    self.vel[0] = self.walkDir
    self.vel[1] = -1 if self.isJumping else 0

    self.vel *= .5

    Entity.update(self, dt)