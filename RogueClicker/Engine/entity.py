import numpy as np, pygame as pg

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

class DynEntity(Entity):
  """Represents a free-moving entity"""
  def __init__(self, world, pos, vel, surf, scl, *groups):
    """Creates a new instance of DynEntity"""
    Entity.__init__(self, world, pos, vel, surf, scl, *groups)

    self.isOnGround = False

  def update(self, dt):
    """Updates the entity every frame"""
    self.vel[1] += .001 * dt

    self.vel[0] *= .5 ** (dt * (.5 if self.isOnGround else .001))

    Entity.update(self, dt)

    self.isOnGround = False