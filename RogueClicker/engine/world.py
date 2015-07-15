from engine.drawable import *
import pygame as pg

class World(Drawable):
  def __init__(self, surf):
    self.surf = surf

    self.bkgdSprites = pg.sprite.LayeredDirty()
    self.envSprites = pg.sprite.LayeredDirty()
    self.dynSprites = pg.sprite.LayeredDirty()


  def updatePhys(self, dt):
    for sprite in self.dynSprites:
      print(sprite)
      #print(pg.sprite.spritecollide(sprite,
      #                              self.envSprites[0],
      #                              self.envSprites,
      #                              False, 
      #                              lambda a, b: pg.sprite.collide_mask(a, b)))
    pass

  def draw(self, dt):
    self.bkgdSprites.update(dt)

    pg.display.update(self.bkgdSprites.draw(self.surf, self.surf))

    pg.display.update(self.envSprites.draw(self.surf, self.surf))

    pg.display.update(self.dynSprites.draw(self.surf, self.surf))