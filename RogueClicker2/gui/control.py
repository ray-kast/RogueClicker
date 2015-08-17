from engine.drawable import *

class Control(Drawable):
  def __init__(self):
    self._isMouseOver = False
    self._isMouseDown = False
  
  @property
  def _IsMouseOver(self):
    raise NotImplementedError()

  @_IsMouseOver.setter
  def _IsMouseOver(self, value):
    raise NotImplementedError()

  @property
  def _IsMouseDown(self):
    raise NotImplementedError()

  @_IsMouseDown.setter
  def _IsMouseDown(self, value):
    raise NotImplementedError()

  def hitTest(self, point):
    raise NotImplementedError()

  def _mouseMove(self, point):
    self._IsMouseOver = self.hitTest(point)

    return self._IsMouseOver

  def _mouseDown(self):
    if self._IsMouseOver: self._IsMouseDown = True

    return self._IsMouseOver

  def _mouseUp(self):
    if self._IsMouseDown:
      self._IsMouseDown = False
      return True

    return False

class ControlList(Drawable):
  def __init__(self):
    self._controls = []

  def add(self, control):
    self._controls.append(control)

  def remove(self, control):
    self._controls.remove(control)

  def mouseMove(self, point):
    for control in self._controls:
      if control._mouseMove(point):
        return True

    return False

  def mouseDown(self):
    for control in self._controls:
      if control._mouseDown():
        return True

    return False

  def mouseUp(self):
    for control in self._controls:
      if control._mouseUp():
        return True

    return False

  def draw(self, game, dt):
    for control in self._controls:
      control.draw(game, dt)