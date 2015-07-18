from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, world, pos, vel, *groups):
    self.defImg = pg.image.load("assets\\sprites\\player.png")
    self.jumpImg = pg.image.load("assets\\sprites\\playerJumping.png")
    self.crouchImg = pg.image.load("assets\\sprites\\playerCrouch.png")

    Mob.__init__(self, world, pos, vel, self.defImg, 1, *groups)

    self.walkFrame = []
    self.shootFrame = []
    self.loadWalk()
    self.loadShoot()
    self.walk_f = 0

    self.initPos = self.pos.copy()
    self.initVel = self.vel.copy()
    self.inAir = False

  def update(self, dt):
    if self.walk_f >= 8: self.walk_f = 0

    keys = pg.key.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    self.isJumping = keys[pg.K_SPACE] or keys[pg.K_w]
    self.image = self.defImg if not self.isJumping else self.jumpImg 
    
    if self.isJumping: self.inAir = True
    if self.isOnGround: self.inAir = False
    
    if self.walkDir > 0:
      self.image = self.walkFrame[self.walk_f]
    if self.walkDir < 0:
      self.image = self.walkFrame[self.walk_f]
      self.image = pg.transform.flip(self.image, True, False)

    if self.inAir: self.image = self.crouchImg

    if keys[pg.K_v]:
      self.walkDir = 0
      self.shoot()
      if keys[pg.K_a]: self.image = pg.transform.flip(self.image, True, False)

    Mob.update(self, dt)

    if not self.world.rect.colliderect(self.rect):
      self.pos = self.initPos.copy()
      self.vel = self.initVel.copy()

    self.walk_f += 1

  def loadWalk(self):
    for i in range(8):
      self.walkFrame.append(pg.image.load("assets\\sprites\\walkFrames\\Player_F" + str(i) + ".png"))

  def loadShoot(self):
    for n in range(3):
      self.shootFrame.append(pg.image.load("assets\\sprites\\shootFrames\\playerPistol_f" + str(n) + ".png"))

  def shoot(self):
    if self.image != self.shootFrame[2]:
      self.image = self.shootFrame[0]
      self.image = self.shootFrame[1]
      self.image = self.shootFrame[2]
    else: self.image = self.shootFrame[2]
    
