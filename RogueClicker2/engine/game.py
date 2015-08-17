import pygame as pg
import pygame.time as pt

class Game:
  def __init__(self, fps = 120):
    self.clock = pt.Clock()
    self._proc = None
    self._doQuit = False
    self.fps = fps
    self.surf = None

    pg.init()

    pg.mixer.init()

  @property
  def Process(self):
    return self._proc

  @Process.setter
  def Process(self, value):
    value._onAttach(self)

    self._proc = value

  def _init(self):
    info = pg.display.Info()

    self.surf = pg.display.set_mode((info.current_w, info.current_h), pg.FULLSCREEN | pg.DOUBLEBUF | pg.HWSURFACE)

  def _deinit(self):
    pg.mixer.quit()

    pg.quit()

  def quit(self):
    self._doQuit = True

  def run(self):
    self._init()

    self.clock.tick()

    doBreak = False
    while True:
      dt = self.clock.tick(self.fps)

      for event in pg.event.get():
        if event.type == pg.QUIT:
          self.quit()
        elif self._proc != None:
          self._proc.event(self, event, dt)

      if self._doQuit: break

      if self._proc != None: self._proc.draw(self, dt)

      if self._doQuit: break

      pg.display.flip()

    self._deinit()