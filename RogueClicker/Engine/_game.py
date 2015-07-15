import pygame as pg

class Game(object):
  __curr__ = None

  def __new__():
    if __curr__ == None:
      __curr__ = object()

    return __curr__

  def __init__(self):
    self.scrRect = pg.Rect(0, 0, 0, 0)
    self.win = None

  def init(self):
    pg.init()

    info = pg.display.Info()

    self.scrRect.width = info.current_w
    self.scrRect.height = info.current_h

    flags = pg.HWSURFACE | pg.FULLSCREEN

    if not __debug__:
      flags |= pg.FULLSCREEN

    self.win = pg.display.set_mode(self.scrRect.size, flags)

    return True

  def run(self):
    if not self.init():
      return False

    

    return True