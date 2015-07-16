import pygame as pg

class Entity(pg.sprite.DirtySprite):
  def __init__(self, pos, img, *groups):
    pg.sprite.DirtySprite.__init__(self, *groups)

    self.image = pg.image.load(img)

    self.rect = self.source_rect = self.image.get_rect()

    self.move(pos)

  def move(self, pos):
    self.rect.topleft = pos

    self.dirty = 1

  def draw(self, surf, dt):
    surf.blit(self.image, self.rect.topleft)