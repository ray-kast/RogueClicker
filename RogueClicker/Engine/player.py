from engine.color import *
from engine.mob import *
import pygame as pg

class Player(Mob):
  def __init__(self, pos, *groups):
    Mob.__init__(self, pos, pg.image.load("assets\\sprites\\test.png"), 4, *groups)

  def update(self, dt):
    keys = pg.key.get_pressed()
    if keys[pg.K_a]: self.walkDir = -1
    elif keys[pg.K_d]: self.walkDir = 1
    else: self.walkDir = 0

    self.isJumping = keys[pg.K_SPACE]

    Mob.update(self, dt)
