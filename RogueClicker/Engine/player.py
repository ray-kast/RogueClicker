from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, world, pos, vel, *groups):
    Mob.__init__(self, world, pos, vel, pg.image.load("assets\\sprites\\test.png"), 4, *groups)
    self.initPos = self.pos.copy()
    self.initVel = self.vel.copy()

  def update(self, dt):
    keys = pg.key.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    self.isJumping = keys[pg.K_SPACE]

    Mob.update(self, dt)

    if not self.world.rect.colliderect(self.rect):
      self.pos = self.initPos.copy()
      self.vel = self.initVel.copy()