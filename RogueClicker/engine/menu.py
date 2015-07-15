from engine.drawable import *
import pygame as pg, pygame.gfxdraw as gd

class Menu(Drawable):
  def __init__(self, surf):
     Drawable.__init__(self, surf)
     self.surf = surf
     self.menuitemclicked = False
     self.buttons = []

  def add(self, btn):
    self.buttons.append(btn)

  def event(self, event, game, dt):
    if event.type == pg.MOUSEBUTTONDOWN:
      pos = pg.mouse.get_pos()
      for button in self.buttons:
        if button.rect.collidepoint(pos):
          button.click()
          break

  def draw(self, game, dt):
    self.surf.fill((0, 0, 0))

    for button in self.buttons:
      button.draw(game, dt)

  class Button(Drawable):
    def __init__(self, menu, cmd, bkgd, fore, text, pos, size):
      Drawable.__init__(self, menu.surf)

      menu.add(self)

      self.rect = pg.Rect(pos, size)

      self.cmd = cmd

      self.fore = fore
      self.bkgd = bkgd

    def draw(self, game, dt):
      self.surf.fill(self.bkgd, self.rect)

    def click(self):
      self.cmd(self)