import traceback
from engine.dummysprite import *
from engine.game import *
from engine.world import *
from test import *

try:
  game = TestGame()

  game.run()

except AttributeError as e:
  print("Caught {0}: {1}\n{2}".format(type(e).__name__, e, "".join(traceback.format_tb(e.__traceback__))))

  raise e