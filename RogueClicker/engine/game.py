import pygame as pg
from engine.color import *

class Game:
  """Encapsulates the base logic of a game"""
  __curr__ = None

  def __new__(cls):
    """Creates exactly one instance of Game"""
    if Game.__curr__ == None:
      Game.__curr__ = super(Game, cls).__new__(cls)

    return Game.__curr__

  def __init__(self):
    """Initializes the current instance of Game"""
    self.scrRect = pg.Rect(0, 0, 0, 0)
    self.win = None
    self.clock = pg.time.Clock()
    
    self.doQuit = False
    self.currDrawing = None

  def init(self):
    """Performs initialization at the start of the game"""
    pg.init()

    info = pg.display.Info()

    self.scrRect.width = info.current_w
    self.scrRect.height = info.current_h

    self.win = pg.display.set_mode((1600, 900), pg.HWSURFACE | pg.DOUBLEBUF | pg.FULLSCREEN)

  def deinit(self):
    """Performs cleanup at the end of the game"""
    pg.quit()

  def postQuit(self):
    """Post a request for the game to quit"""
    self.doQuit = True

  def run(self):
    """Launch the game"""
    self.init()
        
    self.win.fill(Colors.Green)

    self.clock.tick()

    while True:
      dt = self.clock.tick()
      
      for event in pg.event.get():
        if event.type == pg.QUIT:
          self.postQuit()
          continue
        
        elif event.type == pg.KEYDOWN:
          if event.key == pg.K_p:
            pg.image.save(self.win, "assets\\screenshot.png")
            continue

        self.currDrawing.event(event, self, dt)

      if self.doQuit: break
      
      if self.currDrawing != None:
        self.currDrawing.draw(self, dt)

      pg.display.flip()

      if self.doQuit: break

    self.deinit()
