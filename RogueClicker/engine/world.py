import pygame as pg
import numpy as np
from engine.drawable import *
from engine.entity import *
from engine.color import *
from engine import levelloader
import os
class World(Drawable):
  """Manages the player, entities, and environment of the levels"""
  def __init__(self, surf):
    """Create a new instance of World"""
    Drawable.__init__(self, surf)

    basePath = "assets\\levels"
    self.dirs = os.listdir(basePath)
    self.files = []
    for dir in self.dirs:
      
      path = os.path.join(basePath, dir)
      if os.path.isdir(path):
          for file in os.listdir(path):
            fpath = os.path.join(path, file)

            if os.path.isfile(fpath):
              split = os.path.splitext(fpath)

              if split[1] == ".png":
                self.files.append(fpath)

    print(self.files)
    self.bkgdSprites = pg.sprite.LayeredUpdates()
    self.envSprites = pg.sprite.LayeredUpdates()
    self.dynSprites = pg.sprite.LayeredUpdates()

    self.rect = self.surf.get_rect()

    self.playerSpawn = np.array([0, 0], np.float)
    self.vEnts = []
    self.player = None

    img = pg.image.load("assets\\sprites\\blocks\\metalSheet32x32.png")
    size = np.multiply(img.get_rect().size, 2)
    scSize = self.surf.get_rect().size

    img = pg.transform.scale(img, size)

    bkSurf = pg.Surface(scSize)

    for row in range(0, scSize[1], size[1]):
      for col in range(0, scSize[0], size[0]):
        bkSurf.blit(img, (col, row))

    self.bkgd = Entity(self, (0, 0), (0, 0), bkSurf, 1)

    self.bkgdSprites.add(self.bkgd, layer = 0)

    self.levelcount = 0

  def advance(self, game):
    print(self.levelcount, "/", len(self.files))

    if self.levelcount >= len(self.files):
      game.postQuit()
      return

    self.bkgdSprites.remove(s for s in self.bkgdSprites if s != self.bkgd)
    self.envSprites.remove(s for s in self.envSprites)
    self.dynSprites.remove(s for s in self.dynSprites if s != self.player)

    self.surf.fill(Colors.Green)

    self.pic = pg.image.load(self.files[self.levelcount])
    level = levelloader.level(self.pic, self)
    self.blocks = level.getblocks

    self.player.spawn()

    self.levelcount += 1

  def draw(self, game, dt):
    """Called when the attached Game draws a frame"""
    dMouse = np.subtract(pg.mouse.get_pos(), self.rect.center)
    pg.mouse.set_pos(self.rect.centerx, self.rect.centery)

    self.bkgdSprites.update(dt)
    self.envSprites.update(dt)
    self.dynSprites.update(dt, dMouse)
    
    for ent in self.vEnts:
      if self.player.rect.colliderect(ent.rect):
        self.advance(game)

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