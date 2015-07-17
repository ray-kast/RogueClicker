from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, world, pos, vel, *groups):
    Mob.__init__(self, world, pos, vel, pg.image.load("assets\\sprites\\test.png"), 4, *groups)

  def update(self, dt):
    keys = pg.key.get_pressed()

    self.walkDir = keys[pg.K_d] - keys[pg.K_a]

    self.isJumping = keys[pg.K_SPACE]

    Mob.update(self, dt)
