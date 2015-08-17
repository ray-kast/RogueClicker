from engine.game import *
from engine.gameprocess import *
from gui.controls import *
from gui.gui import *
from gui.keyboard import *
import traceback

import pygame as pg

class Test(GameProcess):
  def event(self, game, event, dt):
    if event.type == pg.KEYDOWN \
      and event.key == pg.K_ESCAPE:
      game.quit()

  def draw(self, game, dt):
    pass

try:
  game = Game()

  mainMenu = Gui()

  mainMenu.keyCmds.add(KeyCommand(lambda: game.quit(), pg.K_ESCAPE))

  btnStyle = ButtonStyle((0, 0, 0), (255, 255, 255), (255, 255, 255),
                         (99, 98, 87), (125, 122, 106), (209, 55, 2),
                         pg.font.SysFont("Arial", 16, False, False))

  mainMenu.controls.add(Button(lambda: None, (10, 10), (300, 32), btnStyle, "Play"))
  mainMenu.controls.add(Button(lambda: None, (10, 52), (300, 32), btnStyle, "Options"))
  mainMenu.controls.add(Button(lambda: game.quit(), (10, 94), (300, 32), btnStyle, "Quit"))

  game.Process = mainMenu

  game.run()

except BaseException as e:
  print("Caught {0}: {1}\n{2}".format(type(e).__name__, e, "".join(traceback.format_tb(e.__traceback__))))

  raise e