import engine.game as gm, engine.dummysprite as ds, traceback

try:
  game = gm.Game()

  game.statSprites.add(ds.DummySprite((10, 10)))

  game.run()
except BaseException as e:
  print("Caught {0}: {1}\n{2}".format(type(e).__name__, e, "".join(traceback.format_tb(e.__traceback__))))

  raise e