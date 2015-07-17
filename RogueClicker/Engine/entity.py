import numpy as np, pygame as pg

class Entity(pg.sprite.DirtySprite):
  def __init__(self, pos, surf, scl, *groups):
    pg.sprite.DirtySprite.__init__(self, *groups)

    self.image = pg.transform.scale(surf, np.multiply(surf.get_rect().size, scl))

    self.rect = self.source_rect = self.image.get_rect()

    self.move(pos)

  def move(self, pos):
    self.rect = pg.Rect(pos, self.rect.size)

    self.dirty = 1

  def draw(self, surf, dt):
    surf.blit(self.image, self.rect.topleft)