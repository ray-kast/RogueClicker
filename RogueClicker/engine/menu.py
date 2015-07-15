from engine.drawable import *
import pygame as pg, pygame.gfxdraw as gd

class Menu(Drawable):
  def __init__(self, surf):
     Drawable.__init__(self, surf)
     self.surf = surf
     self.menuitemclicked = False
     self.buttons = []
    #TODO: Add construction code here
  def add(self, btn):
    
    self.buttons.append(btn)

  def event(self, event, dt):
    if event.type == pg.MOUSEBUTTONDOWN:
      pos = pg.mouse.get_pos()
      for button in self.buttons:
        if button.rect.collidepoint(pos):
          button.click()
          break

  def draw(self, dt):
    self.surf.fill((0, 0, 0))

    for button in self.buttons:
      button.draw(dt)


  class Button(Drawable):
    def __init__(self, menu, backgroundcolor, textcolor, text, size, location):
      Drawable.__init__(self, menu.surf)

      self.rect = pg.Rect(location, size)

      self.bkgd = backgroundcolor

    def draw(self, dt):
      self.surf.fill(self.bkgd, self.rect)
        
