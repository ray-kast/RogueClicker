﻿from engine.drawable import *
import pygame as pg

class World(Drawable):
  def __init__(self, surf):
    self.surf = surf

    self.bkgdSprites = pg.sprite.LayeredDirty()
    self.envSprites = pg.sprite.LayeredDirty()
    self.dynSprites = pg.sprite.LayeredDirty()

  def updatePhys(self, dt):
    pass

  def draw(self, game, dt):
    self.bkgdSprites.update(dt)
    self.envSprites.update(dt)
    self.dynSprites.update(dt)

    pg.display.update(self.bkgdSprites.draw(self.surf, self.surf))

    pg.display.update(self.envSprites.draw(self.surf, self.surf))

    pg.display.update(self.dynSprites.draw(self.surf, self.surf))