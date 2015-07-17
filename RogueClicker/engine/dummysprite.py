import pygame as pg
from engine.color import *
from engine.entity import *

class DummySprite(Entity):
  def __init__(self, pos, *groups):
    surf = pg.Surface((100, 100), pg.HWSURFACE | pg.SRCALPHA)

    surf.fill(Colors.Black)

    Entity.__init__(self, pos, surf, 1, *groups)

    #self.source_rect = self.image.get_rect()

    #self.rect = self.source_rect

    #self.rect.topleft = pos