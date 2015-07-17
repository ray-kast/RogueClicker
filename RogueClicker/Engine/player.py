from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, world, pos, vel, *groups):
    self.defImg = pg.image.load("assets\\sprites\\player.png")
    self.jumpImg = pg.image.load("assets\\sprites\\playerJumping.png")
    Mob.__init__(self, world, pos, vel, self.defImg, 1, *groups)
    self.initPos = self.pos.copy()
    self.initVel = self.vel.copy()

  def update(self, dt):
    keys = pg.key.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    self.isJumping = keys[pg.K_SPACE]

    self.image = self.defImg if not self.isJumping else self.jumpImg
    
    Mob.update(self, dt)

    if not self.world.rect.colliderect(self.rect):
      self.pos = self.initPos.copy()
      self.vel = self.initVel.copy()