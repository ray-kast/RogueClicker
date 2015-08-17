import copy
from gui.control import *
import pygame as pg

class ButtonStyle:
  def __init__(self, normalFore, hoverFore, activeFore, normalBkgd, hoverBkgd, activeBkgd, font):
    self.normalFore = normalFore
    self.hoverFore = hoverFore
    self.activeFore = activeFore
    self.normalBkgd = normalBkgd
    self.hoverBkgd = hoverBkgd
    self.activeBkgd = activeBkgd
    self.font = font

  def clone(self):
    return copy.copy(self)

class Button(Control):
  def __init__(self, func, pos, size, style, text):
    Control.__init__(self)

    self.func = func
    self.rect = pg.Rect(pos, size)
    self.textStr = text

    self.normalFore = style.normalFore
    self.hoverFore = style.hoverFore
    self.activeFore = style.activeFore
    self.normalBkgd = style.normalBkgd
    self.hoverBkgd = style.hoverBkgd
    self.activeBkgd = style.activeBkgd
    self.font = style.font
    
    self._recolor()

  @property
  def _IsMouseOver(self):
    return self._isMouseOver

  @_IsMouseOver.setter
  def _IsMouseOver(self, value):
    if value != self._isMouseOver:
      self._isMouseOver = value

      self._recolor()

  @property
  def _IsMouseDown(self):
    return self._isMouseDown

  @_IsMouseDown.setter
  def _IsMouseDown(self, value):
    if value != self._isMouseDown:
      self._isMouseDown = value

      self._recolor()

  def _recolor(self):
    self._currBkgd = (self.activeBkgd if self._IsMouseDown else self.hoverBkgd) if self._IsMouseOver else self.normalBkgd
    self.text = self.font.render(self.textStr, True, (self.activeFore if self._IsMouseDown else self.hoverFore) if self._IsMouseOver else self.normalFore)

  def hitTest(self, point):
    return self.rect.collidepoint(point)

  def _mouseUp(self):
    if self._IsMouseOver and self._IsMouseDown: self.func()
    
    return Control._mouseUp(self)

  def draw(self, game, dt):
    game.surf.fill(self._currBkgd, self.rect)
    game.surf.blit(self.text, self.rect.topleft)