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
    
    self.doQuit = False
    self.currDrawing = None

  def init(self):
    pg.init()

    info = pg.display.Info()

    self.scrRect.width = info.current_w
    self.scrRect.height = info.current_h

    flags = pg.HWSURFACE | pg.DOUBLEBUF | pg.FULLSCREEN

    self.win = pg.display.set_mode(self.scrRect.size, flags)

  def deinit(self):
    pg.quit()

  def postQuit(self):
    self.doQuit = True

  def run(self):
    self.init()
        
    self.win.fill(Colors.Green)

    self.clock.tick()

    while True:
      dt = self.clock.tick(120)
      
      for event in pg.event.get():
        if event.type == pg.QUIT:
          self.postQuit()
        
        elif event.type == pg.KEYDOWN:
          if event.key == pg.K_ESCAPE:
            self.postQuit()

        else: self.currDrawing.event(event, self, dt)

      if self.doQuit: break
      
      self.draw(dt)

      pg.display.flip()

      if self.doQuit: break

    self.deinit()

  def draw(self, dt):
    if self.currDrawing != None:
      self.currDrawing.draw(self, dt)

