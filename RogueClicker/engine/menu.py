import numpy as np, pygame as pg, pygame.gfxdraw as gd
from engine.color import *
from engine.drawable import *

class Menu(Drawable):
  def __init__(self, surf):
     Drawable.__init__(self, surf)
     self.surf = surf
     self.menuitemclicked = False
     self.buttons = []
     self.active = None

  def add(self, btn):
    self.buttons.append(btn)

  def event(self, event, game, dt):
    if event.type == pg.MOUSEMOTION:
      pos = pg.mouse.get_pos()
      for button in self.buttons:
        button.IsHovered = button.rect.collidepoint(pos)

    elif event.type == pg.MOUSEBUTTONDOWN:
      if event.button == 1:
        pos = pg.mouse.get_pos()
        for button in self.buttons:
          if button.IsHovered:
            button.IsActive = True

    elif event.type == pg.MOUSEBUTTONUP:
      if event.button == 1:
        pos = pg.mouse.get_pos()
        for button in self.buttons:
          if button.IsHovered or button.IsActive:
            button.IsActive = False

  def draw(self, game, dt):
    self.surf.fill((0, 0, 0))

    for button in self.buttons:
      button.draw(game, dt)

  class Button:
    def __init__(self, menu, cmd, normal, hover, active, font, text, pos, size):
      self.surf = menu.surf

      menu.add(self)

      self.rect = pg.Rect(pos, size)

      self.cmd = cmd

      self.normal = normal
      self.hover = hover
      self.active = active

      self.font = font
      self.text = text

      self.textSurf = self.font.render(text, False, (0, 0, 0))
      self.textPos = np.subtract(self.rect.center, self.textSurf.get_rect().center)

      self.colors = self.normal
      self.isHovered = False

      self.isActive = False
      
      self.recolor()

    @property
    def IsHovered(self):
      return self.isHovered

    @IsHovered.setter
    def IsHovered(self, value):
      if self.isHovered != value:
        if value: self.mouseOver()
        else: self.mouseOut()
        self.isHovered = value
        self.recolor()

    @property
    def IsActive(self):
      return self.isActive

    @IsActive.setter
    def IsActive(self, value):
      if self.isActive != value:
        if value: self.mouseDown()
        else: self.mouseUp()

        self.isActive = value
        self.recolor()

    def recolor(self):
      self.colors = (self.active if self.isActive else self.hover) \
        if self.isHovered else self.normal

      self.textSurf = self.font.render(self.text, True, self.colors[1])

    def draw(self, game, dt):
      self.surf.fill(self.colors[0], self.rect)

      self.surf.blit(self.textSurf, self.textPos)

    def mouseDown(self):
      pass

    def mouseUp(self):
      if self.IsHovered:
        self.cmd(self)

    def mouseOver(self):
      pass

    def mouseOut(self):
      pass