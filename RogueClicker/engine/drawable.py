class Drawable:
  def __init__(self, surf):
    self.surf = surf

  def draw(self, game, dt):
    pass

  def event(self, event, game, dt):
    return False