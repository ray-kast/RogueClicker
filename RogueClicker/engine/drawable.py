class Drawable:
  """Represents logic to be hosted by a Game class"""

  def __init__(self, surf):
    """Create a new instance of Drawable"""
    self.surf = surf

  def draw(self, game, dt):
    """Called for every frame drawn by Game"""
    pass

  def event(self, event, game, dt):
    """Called for every event handled by Game"""
    return False