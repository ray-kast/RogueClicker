import pygame as pg
from engine.color import *

class DummySprite(pg.sprite.DirtySprite):
  def __init__(self, pos, *groups):
    pg.sprite.DirtySprite.__init__(self, *groups)

    self.image = pg.Surface((100, 100), pg.HWSURFACE | pg.SRCALPHA)

    self.image.fill(Colors.Black)

    self.source_rect = self.image.get_rect()

    self.rect = self.source_rect

    self.rect.topleft = pos