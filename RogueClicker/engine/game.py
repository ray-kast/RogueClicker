import pygame as pg
from engine.color import *

class Game:
  __curr__ = None

  def __new__(cls):
    if Game.__curr__ == None:
      Game.__curr__ = super(Game, cls).__new__(cls)

    return Game.__curr__

  def __init__(self):
    self.scrRect = pg.Rect(0, 0, 0, 0)
    self.win = None
    self.clock = pg.time.Clock()

    self.currDrawing = None

  def init(self):
    pg.init()

    info = pg.display.Info()

    self.scrRect.width = info.current_w
    self.scrRect.height = info.current_h

    flags = pg.HWSURFACE | pg.DOUBLEBUF

    if not __debug__:
      flags |= pg.FULLSCREEN

    self.win = pg.display.set_mode(self.scrRect.size, flags)

  def deinit(self):
    pg.quit()

  def run(self):
    self.init()
        
    self.win.fill(Colors.Green)

    self.clock.tick()

    doRun = True
    while doRun:
      dt = self.clock.tick(120)
      
      for event in pg.event.get():
        if event.type != pg.NOEVENT:
          if event.type == pg.QUIT:
            doRun = False
        
          elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
              doRun = False

          else:
            doRun = self.currDrawing.event(event, dt)
            if not doRun: break

      if not doRun: break

      if not self.draw(): break

      pg.display.flip()

    self.deinit()

  def draw(self):
    if self.currDrawing != None:
      self.currDrawing.draw(dt)

