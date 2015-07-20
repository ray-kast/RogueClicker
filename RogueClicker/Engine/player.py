from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, world, *groups):
    self.defImg = pg.image.load("assets\\sprites\\player.png")
    self.jumpImg = pg.image.load("assets\\sprites\\playerJumping.png")
    self.crouchImg = pg.image.load("assets\\sprites\\playerCrouch.png")

    self.initVel = np.array((0, 0), np.float)

    Mob.__init__(self, world, world.playerSpawn, self.initVel.copy(), self.defImg, 1, *groups)

    self.faceLeft = False
    self.walkFrame = []
    self.shootFrame = []
    self.loadWalk()
    self.loadShoot()
    self.walk_f = 0

    self.inAir = False

  def update(self, dt):
    if self.walk_f >= 8: self.walk_f = 0

    keys = pg.key.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    self.isJumping = keys[pg.K_SPACE] or keys[pg.K_w]
    self.image = self.defImg if not self.isJumping else self.jumpImg 
    
    if self.isJumping: self.inAir = True
    if self.isOnGround: self.inAir = False
    
    if self.walkDir > 0: self.faceLeft = False
     
    if self.walkDir < 0: self.faceLeft = True

    if self.faceLeft and self.walkDir < 0:
      self.image = self.walkFrame[self.walk_f]
      self.image = pg.transform.flip(self.image, True, False)
    elif self.faceLeft:
      self.image = self.defImg
      self.image = pg.transform.flip(self.image, True, False)
    elif not self.faceLeft and self.walkDir > 0:
      self.image = self.walkFrame[self.walk_f]

    if self.inAir and self.faceLeft:
      self.image = self.crouchImg
      self.image = pg.transform.flip(self.image, True, False)
    elif self.inAir:
      self.image = self.crouchImg

    if keys[pg.K_v]:
      self.walkDir = 0
      self.shoot()
      if self.faceLeft: self.image = pg.transform.flip(self.image, True, False)

    Mob.update(self, dt)

    if not self.world.rect.colliderect(self.rect):
      self.pos = self.world.playerSpawn.copy()
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
    
