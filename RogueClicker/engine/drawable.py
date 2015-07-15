class Drawable:
  def __init__(self, surf):
    self.surf = surf

  def draw(self, dt):
    pass

  def event(self, event, dt):
    return False