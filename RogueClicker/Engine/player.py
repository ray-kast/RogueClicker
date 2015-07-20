from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, world, pos, vel, *groups):
    self.defImg = pg.image.load("assets\\sprites\\player.png")
    self.jumpImg = pg.image.load("assets\\sprites\\playerJumping.png")
    self.crouchImg = pg.image.load("assets\\sprites\\playerCrouch.png")

    Mob.__init__(self, world, pos, vel, self.defImg, 1, *groups)

    self.faceLeft = False
    self.walkFrames = []
    self.shootFrames = []
    self.walk_f = 0

    self.walkTime = 0
    self.numWalkFrames = 8
    self.walkFrameSpeed = .01

    self.loadWalk()
    self.loadShoot()

    self.initPos = self.pos.copy()
    self.initVel = self.vel.copy()
    self.inAir = False

  def update(self, dt):
    keys = pg.key.get_pressed()
    btns = pg.mouse.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    self.isJumping = keys[pg.K_SPACE] or keys[pg.K_w]

    self.image = self.defImg if not self.isJumping else self.jumpImg 
    
    if self.isJumping: self.inAir = True
    elif self.isOnGround: self.inAir = False
    
    if self.walkDir > 0: self.faceLeft = False
    elif self.walkDir < 0: self.faceLeft = True

    if not self.isOnGround:
      self.image = self.crouchImg
    
    if self.walkDir:
      self.walkTime = (self.walkTime + (dt * self.walkFrameSpeed)) % self.numWalkFrames
      self.image = self.walkFrames[int(self.walkTime)]
    else: self.walkTime = 0

    if self.faceLeft:
      self.image = pg.transform.flip(self.image, True, False)

    if btns[0] or keys[pg.K_v]:
      self.walkDir = 0
      self.shoot()
      if self.faceLeft: self.image = pg.transform.flip(self.image, True, False)

    Mob.update(self, dt)

    if self.rect.right < self.world.rect.left \
      or self.rect.left > self.world.rect.right \
      or self.rect.top > self.world.rect.bottom:
      self.pos = self.initPos.copy()
      self.vel = self.initVel.copy()

    self.walk_f += 1

  def loadWalk(self):
    for i in range(self.numWalkFrames):
      self.walkFrames.append(pg.image.load("assets\\sprites\\walkFrames\\Player_F" + str(i) + ".png"))

  def loadShoot(self):
    for n in range(3):
      self.shootFrames.append(pg.image.load("assets\\sprites\\shootFrames\\playerPistol_f" + str(n) + ".png"))

  def shoot(self):
    if self.image != self.shootFrames[2]:
      self.image = self.shootFrames[0]
      self.image = self.shootFrames[1]
      self.image = self.shootFrames[2]
    else: self.image = self.shootFrames[2]
    
