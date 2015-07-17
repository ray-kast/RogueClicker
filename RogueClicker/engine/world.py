from engine.drawable import *
from engine.color import *
import pygame as pg

class World(Drawable):
  """Manages the player, entities, and environment of the levels"""
  def __init__(self, surf):
    """Create a new instance of World"""
    Drawable.__init__(self, surf)

    self.bkgdSprites = pg.sprite.LayeredUpdates()
    self.envSprites = pg.sprite.LayeredUpdates()
    self.dynSprites = pg.sprite.LayeredUpdates()

  def draw(self, game, dt):
    """Called when the attached Game draws a frame"""
    self.surf.fill(Colors.Green)

    self.bkgdSprites.update(dt)
    self.envSprites.update(dt)
    self.dynSprites.update(dt)

    self.bkgdSprites.draw(self.surf)
    self.envSprites.draw(self.surf)
    self.dynSprites.draw(self.surf)