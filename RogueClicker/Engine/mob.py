from engine.entity import *

class Mob(Entity):
  def __init__(self, *groups):
    Entity.__init__(self, *groups)

    self.isOnGround = False
    self.__pos__ = [0, 0]

    self.walkDir = 0
    self.isJumping = False

  @property
  def Pos(self):
    return self.__pos__

  @property
  def Pos(self, value):
    self.__pos__ = value

    self.move(pos)