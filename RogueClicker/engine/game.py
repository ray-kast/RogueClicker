import pygame as pg
from engine.color import *

class Game(object):
  __curr__ = None

  def __new__(cls):
    if Game.__curr__ == None:
      Game.__curr__ = super(Game, cls).__new__(cls)

    return Game.__curr__

  def __init__(self):
    self.scrRect = pg.Rect(0, 0, 0, 0)
    self.win = None
    self.clock = pg.time.Clock()

    self.statSprites = pg.sprite.LayeredDirty()
    self.dynSprites = pg.sprite.LayeredDirty()

  def init(self):
    pg.init()

    info = pg.display.Info()

    self.scrRect.width = info.current_w
    self.scrRect.height = info.current_h

    flags = pg.HWSURFACE | pg.DOUBLEBUF

    if not __debug__:
      flags |= pg.FULLSCREEN

    self.win = pg.display.set_mode(self.scrRect.size, flags)

    pg.mouse.set_visible(False)

  def deinit(self):
    pg.quit()

  def run(self):
    self.init()
        
    self.win.fill(Colors.Green)

    self.clock.tick()

    while True:
      event = pg.event.poll()
      if event.type != pg.NOEVENT:
        if event.type == pg.QUIT:
          break
        
        elif event.type == pg.KEYDOWN:
          if event.key == pg.K_ESCAPE:
            break

      else:
        dt = self.clock.tick(120)

        pg.display.update(self.statSprites.draw(self.win, self.win))

        pg.display.update(self.dynSprites.draw(self.win, self.win))

        pg.display.flip()

    self.deinit()