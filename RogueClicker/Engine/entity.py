import numpy as np, pygame as pg

class Entity(pg.sprite.DirtySprite):
  def __init__(self, pos, surf, scl, *groups):
    pg.sprite.DirtySprite.__init__(self, *groups)

    self.image = pg.transform.scale(surf, np.multiply(surf.get_rect().size, scl))

    self.source_rect = self.image.get_rect()

    self.pos = pos
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
    self.Pos = np.add(self.Pos, (dt * .1, 0))

    

  def draw(self, surf, dt):
    surf.blit(self.image, self.rect.topleft)