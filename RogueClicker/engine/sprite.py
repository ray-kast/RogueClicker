import pygame as pg

class GameSprite(pg.sprite.DirtySprite):
  def __init__(self, *groups):
    pg.sprite.DirtySprite.__init__(self, *groups)

    self.rect = pg.Rect()

  def move(self, pos):
    self.rect