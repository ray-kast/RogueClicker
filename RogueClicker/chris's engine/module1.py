import pygame
import os
import sys
import time
clock = pygame.time.Clock()
class Engine():
    def __init__(self):
        pygame.display.init()
        infoObject = pygame.display.Info()
        self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
        self.player = Player([300,300])
        self.game_running = True
    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.left = True
                if event.key == pygame.K_d:
                    self.player.right = True
                if (event.key == pygame.K_w) or (event.key == pygame.K_SPACE):
                    self.player.up = True
                if event.key == pygame.K_s:
                    self.player.down = True
                if event.type == pygame.K_RETURN:
                    self.game_running = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.left = False
                if event.key == pygame.K_d:
                    self.player.right = False
                if (event.key == pygame.K_w) or (event.key == pygame.K_SPACE):
                    self.player.up = False
                if event.key == pygame.K_s:
                    self.player.down = False
                if event.type == pygame.K_ESCAPE:
                    sys.exit()
        if self.player.left == True:
            self.player.move_left()
        if self.player.right == True:
            self.player.move_right()
        if self.player.up == True:
            self.player.move_up()
        if self.player.down == True:
            self.player.move_down()


class Player():
    def __init__(self, posistion):
        self.surface = pygame.image.load(os.path.join('scrap.png'))
        self.posistion = posistion
        self.width = 30
        self.surface.fill([0,0,255])
        self.rect = self.surface.get_rect()
        self.speed = 50
        self.left = False
        self.right = False
        self.up = False
        self.down = False
    def move_left(self):
        self.posistion[0] -= self.speed
        self.draw()
    def move_right(self):
        self.posistion[0] += self.speed
        self.draw()
    def move_up(self):
        self.posistion[1] -= self.speed
        self.draw() 
    def move_down(self):
        self.posistion[1] += self.speed
        self.draw()
    def draw(self):
        engine.screen.fill([0,0,0])
        engine.screen.blit(self.surface, self.posistion)
        
engine = Engine()
while engine.game_running:
    engine.check_input()
    engine.player.draw()
    
    