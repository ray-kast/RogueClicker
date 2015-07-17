import numpy as np, pygame as pg

class Entity(pg.sprite.Sprite):
  def __init__(self, world, pos, vel, surf, scl, *groups):
    pg.sprite.Sprite.__init__(self, *groups)
    
    self.world = world

    self.image = pg.transform.scale(surf, np.multiply(surf.get_rect().size, scl))

    self.source_rect = self.image.get_rect()

    self.pos = np.array(pos)
    self.vel = np.array(vel)
    self.size = self.source_rect.size

  @property
  def rect(self):
    return pg.Rect(self.pos, self.size)

  @property
  def Pos(self):
    return self.pos

  @Pos.setter
  def Pos(self, value):
    self.pos = value

    self.dirty = 1

  def update(self, dt):
    self.pos += self.vel * dt

  def draw(self, surf, dt):
    surf.blit(self.image, self.rect.topleft)