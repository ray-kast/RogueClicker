import pygame as pg, numpy as np
from engine.drawable import *
from engine.color import *

class World(Drawable):
  """Manages the player, entities, and environment of the levels"""
  def __init__(self, surf):
    """Create a new instance of World"""
    Drawable.__init__(self, surf)

    self.bkgdSprites = pg.sprite.LayeredUpdates()
    self.envSprites = pg.sprite.LayeredUpdates()
    self.dynSprites = pg.sprite.LayeredUpdates()

    self.rect = self.surf.get_rect()

    self.playerSpawn = np.array([0, 0], np.float)
    self.playerFinish = np.array([0, 0], np.float)

  def draw(self, game, dt):
    """Called when the attached Game draws a frame"""
    dMouse = np.subtract(pg.mouse.get_pos(), self.rect.center)
    pg.mouse.set_pos(self.rect.centerx, self.rect.centery)

    self.bkgdSprites.update(dt)
    self.envSprites.update(dt)
    self.dynSprites.update(dt)

    for sprite in self.dynSprites:
      spriteCollides = False
      for ent in self.envSprites:
        if sprite.rect.colliderect(ent.rect):
          spriteCollides = True
          if sprite.lastRect.right <= ent.rect.left \
            and sprite.rect.right > ent.rect.left:
            if sprite.vel[0] > 0: sprite.vel[0] *= ent.bounce[0]
            sprite.pos[0] += ent.rect.left - sprite.rect.right

          if sprite.lastRect.left >= ent.rect.right \
            and sprite.rect.left < ent.rect.right:
            if sprite.vel[0] < 0: sprite.vel[0] *= ent.bounce[2]
            sprite.pos[0] += ent.rect.right - sprite.rect.left

          if sprite.lastRect.bottom <= ent.rect.top \
            and sprite.rect.bottom > ent.rect.top:
            if sprite.vel[1] > 0: sprite.vel[1] *= ent.bounce[1]
            sprite.pos[1] += ent.rect.top - sprite.rect.bottom
            sprite.isOnGround = True

          if sprite.lastRect.top >= ent.rect.bottom \
            and sprite.rect.top < ent.rect.bottom:
            if sprite.vel[1] < 0: sprite.vel[1] *= ent.bounce[3]
            sprite.pos[1] += ent.rect.bottom - sprite.rect.top
      
      if not spriteCollides:
        sprite.lastRect = sprite.rect

    self.bkgdSprites.draw(self.surf)
    self.envSprites.draw(self.surf)
    self.dynSprites.draw(self.surf)