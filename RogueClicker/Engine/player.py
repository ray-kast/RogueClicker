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
    self.loadWalk()
    self.i = 0

    self.initPos = self.pos.copy()
    self.initVel = self.vel.copy()
    self.inAir = False

  def update(self, dt):
    if self.i >= 8: self.i = 0
    else: self.i += 1

    keys = pg.key.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    if self.walkDir != 0: self.image = self.walkFrame[self.i] # LIST OUT OF RANGE ERROR - HAVEN'T FIXED YET

    self.isJumping = keys[pg.K_SPACE]
    if self.isJumping: self.inAir = True
    if self.isOnGround: self.inAir = False

    self.image = self.defImg if not self.isJumping else self.jumpImg 
    
    if self.inAir: self.image = self.crouchImg

    Mob.update(self, dt)

    if not self.world.rect.colliderect(self.rect):
      self.pos = self.initPos.copy()
      self.vel = self.initVel.copy()

  def loadWalk(self):
    for i in range(8):
      self.walkFrame.append(pg.image.load("assets\\sprites\\walkFrames\\Player_F" + str(i) + ".png"))
    
