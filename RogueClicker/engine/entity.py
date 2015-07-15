import pygame as pg

class Entity(pg.sprite.DirtySprite):
  def __init__(self, *groups):
    pg.sprite.DirtySprite.__init__(self, *groups)

    self.rect = pg.Rect()

    self.pos = [0, 0]

  def move(self, pos):
    self.rect.topleft = pos

    self.dirty = 1