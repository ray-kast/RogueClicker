from engine.drawable import *
import pygame as pg, pygame.gfxdraw as gd

class Menu(Drawable):
  def __init__(self, surf):
     Drawable.__init__(self, surf)
     self.surf = surf
     self.menuitemclicked = False
     self.buttons = []
     self.hovered = None
     self.active = None

  def add(self, btn):
    self.buttons.append(btn)

  def event(self, event, game, dt):
    if event.type == pg.MOUSEMOTION:
      pos = pg.mouse.get_pos()
      newHovered = None
      for button in self.buttons:
        if button.rect.collidepoint(pos):
          newHovered = button
          break

      if newHovered != self.hovered:
        if newHovered: newHovered.mouseOver()
        if self.hovered: self.hovered.mouseOut()
        self.hovered = newHovered

    elif event.type == pg.MOUSEBUTTONDOWN:
      pos = pg.mouse.get_pos()
      if self.hovered and self.hovered.rect.collidepoint(pos):
        self.hovered.mouseDown()

    elif event.type == pg.MOUSEBUTTONUP:
      pos = pg.mouse.get_pos()
      if self.hovered and self.hovered.rect.collidepoint(pos):
        self.hovered.mouseUp()

  def draw(self, game, dt):
    self.surf.fill((0, 0, 0))

    for button in self.buttons:
      button.draw(game, dt)

  class Button(Drawable):
    def __init__(self, menu, cmd, normal, hover, active, text, pos, size):
      Drawable.__init__(self, menu.surf)

      menu.add(self)

      self.rect = pg.Rect(pos, size)

      self.cmd = cmd

      self.normal = normal
      self.hover = hover
      self.active = active

      self.colors = self.normal
      self.isHovered = False
      self.isActive = False

    def draw(self, game, dt):
      self.surf.fill(self.colors[0], self.rect)

    def mouseDown(self):
      self.colors = self.active

    def mouseUp(self):
      self.colors = self.hover if self.isHovered else self.normal

    def mouseOver(self):
      if not self.isActive:
        self.isHovered = True
        self.colors = self.hover

    def mouseOut(self):
      if not self.isActive:
        self.isHovered = False
        self.colors = self.normal