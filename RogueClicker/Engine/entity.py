import numpy as np
import pygame as pg

class Entity(pg.sprite.Sprite):
  """A base in-game entity"""
  def __init__(self, world, pos, vel, surf, scl, *groups):
    """Create a new instance of Entity"""
    pg.sprite.Sprite.__init__(self, *groups)
    
    self.world = world

    self.image = pg.transform.scale(surf, np.multiply(surf.get_rect().size, scl))

    self.source_rect = self.image.get_rect()

    self.pos = np.array(pos, dtype = np.float)
    self.vel = np.array(vel, dtype = np.float)
    self.size = self.source_rect.size
    
    self.lastRect = self.rect

  @property
  def rect(self):
    """Gets the bounding Rect of this entity"""
    return pg.Rect(self.pos, self.size)

  @property
  def Pos(self):
    """Gets or sets the position of the entity"""
    return self.pos

  @Pos.setter
  def Pos(self, value):
    """Gets or sets the position of the entity"""
    self.pos = value

    self.dirty = 1

  def update(self, dt):
    """Updates the entity every frame"""
    #self.lastRect = self.rect
    self.pos += self.vel * dt

class StaticEntity(Entity):
  def __init__(self, world, pos, vel, surf, scl, *groups):
    Entity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.bounce = np.array([0, 0, 0, 0], dtype = np.float)
    
    self.Bounce = 0
    self.BounceTop = self.BounceBottom = .1

  @property
  def Bounce(self):
    return self.bounce.mean()

  @Bounce.setter
  def Bounce(self, value):
    self.bounce.fill(-value)

  @property
  def BounceLeft(self):
    return self.bounce[0]

  @BounceLeft.setter
  def BounceLeft(self, value):
    self.bounce[0] = -value

  @property
  def BounceTop(self):
    return self.bounce[1]

  @BounceTop.setter
  def BounceTop(self, value):
    self.bounce[1] = -value

  @property
  def BounceRight(self):
    return self.bounce[2]

  @BounceRight.setter
  def BounceRight(self, value):
    self.bounce[2] = -value

  @property
  def BounceBottom(self):
    return self.bounce[3]

  @BounceBottom.setter
  def BounceBottom(self, value):
    self.bounce[3] = -value

class DynEntity(Entity):
  """Represents a free-moving entity"""
  def __init__(self, world, pos, vel, surf, scl, *groups):
    """Creates a new instance of DynEntity"""
    Entity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.isOnGround = False

    self.Gravity = .001
    self.AirFriction = .001
    self.GroundFriction = .15

  @property
  def Gravity(self):
    return self.gravity

  @Gravity.setter
  def Gravity(self, value):
    self.gravity = float(value)

  @property
  def AirFriction(self):
    return self.airFric

  @AirFriction.setter
  def AirFriction(self, value):
    self.airFric = float(value)

  @property
  def GroundFriction(self):
    return self.gndFric

  @GroundFriction.setter
  def GroundFriction(self, value):
    self.gndFric = float(value)

  def update(self, dt):
    """Updates the entity every frame"""
    self.vel[1] += self.gravity * dt

    self.vel[0] *= .5 ** (dt * (self.gndFric if self.isOnGround else self.airFric))
    self.vel[1] *= .5 ** (dt * self.airFric)

    Entity.update(self, dt)

    self.isOnGround = False