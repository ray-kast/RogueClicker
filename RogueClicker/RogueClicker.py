import traceback
from game import *

try:
  game = RogueClickerGame()

  game.run()
except BaseException as e:
  print("Caught {0}: {1}\n{2}".format(type(e).__name__, e, "".join(traceback.format_tb(e.__traceback__))))

  raise e