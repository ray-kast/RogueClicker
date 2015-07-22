import math, numpy as np
from engine.entity import *

class Mob(DynEntity):
  def __init__(self, world, pos, vel, surf, scl, *groups):
    DynEntity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.isOnGround = False

    self.walkDir = 0
    self.isJumping = False

    self.AirSpeed = .75
    self.GroundSpeed = .085
    self.JumpSpeed = 18500

  @property
  def AirSpeed(self):
    return self.airSpeed / self.airFric

  @AirSpeed.setter
  def AirSpeed(self, value):
    self.airSpeed = float(value * self.airFric)

  @property
  def GroundSpeed(self):
    return self.gndSpeed / self.gndFric

  @GroundSpeed.setter
  def GroundSpeed(self, value):
    self.gndSpeed = float(value * self.gndFric)

  @property
  def JumpSpeed(self):
    return -self.jmpSpeed / self.gravity

  @JumpSpeed.setter
  def JumpSpeed(self, value):
    self.jmpSpeed = float(-value * math.sqrt(self.gravity) * self.airFric)

  def updateForces(self, dt):
    DynEntity.updateForces(self, dt)

    self.vel[0] += self.walkDir * (self.gndSpeed if self.isOnGround else self.airSpeed) * dt
    self.vel[1] += self.jmpSpeed if self.isJumping and self.isOnGround else 0

  def updatePos(self, dt):
    DynEntity.updatePos(self, dt)

  def update(self, dt):
    self.updateForces(dt)

    self.updatePos(dt)