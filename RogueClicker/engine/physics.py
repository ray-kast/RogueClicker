class PhysObject(object):
  def __init__(self):
    pass

  def update(self):
    pass

  def tick(self, dt):
    pass

class PhysHost(object):
  def __init__(self):
    self.__objs__ = []

  @property
  def Objects(self):
    return self.__objs__

  def tick(self, dt):
    for obj in self.Objects:
      obj.tick(dt)