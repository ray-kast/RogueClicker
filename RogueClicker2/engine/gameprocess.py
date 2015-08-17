from engine.drawable import *

class GameProcess(Drawable):
  def _onAttach(self, game):
    pass

  def _onDetach(self, game):
    pass

  def event(self, game, event, dt):
    raise NotImplementedError()