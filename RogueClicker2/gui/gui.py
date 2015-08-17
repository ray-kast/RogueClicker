from engine.gameprocess import *
from gui.control import *
from gui.keyboard import *

class Gui(GameProcess):
  def __init__(self):
    self.keyCmds = KeyCommandList()
    self.controls = ControlList()

  def event(self, game, event, dt):
    if event.type == pg.KEYDOWN:
      self.keyCmds.handle(event.key, pg.key.get_mods())

    elif event.type == pg.MOUSEMOTION:
      self.controls.mouseMove(pg.mouse.get_pos())
    
    elif event.type == pg.MOUSEBUTTONDOWN:
      self.controls.mouseDown()

    elif event.type == pg.MOUSEBUTTONUP:
      self.controls.mouseUp()

  def draw(self, game, dt):
    self.controls.draw(game, dt)