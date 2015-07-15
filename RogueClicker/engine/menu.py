from engine.drawable import *

class Menu(Drawable):
  def __init__(self, surf):
    Drawable.__init__(self, surf)

    #TODO: Add construction code here

  def draw(self, dt):
      
    pass #Add drawing code here (dt is delta-time, surf is your surface)
import pygame
import os
import time
class Menu():
    def __init__(self):
        self.screen = pygame.display.set_mode([300,300])
        self.surface = pygame.image.load(os.path.join('bla.png'))
        self.screen.blit(self.surface, [150,150])
        self.menuitemclicked = False
    def detectmouseclick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                    
             
    def menuitempressed(self):
        detectmouseclick()
        
        
menu = Menu()
pygame.display.update()

while True:
    menu.detectmouseclick()
    time.sleep(1)