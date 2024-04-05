"""
Hola este es modulo Bullet,
este modulo manejara los disparon
"""
import pygame
balapng = pygame.image.load("assets/Ducky.png")
balapng_scaled = pygame.transform.scale(balapng,(30,30))

from pygame.locals import (RLEACCEL)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        #Asumamos que esto funciona
        super(Bullet, self).__init__()
        self.surf = balapng_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect(center=(x -10,y +30))
        self.speed = 10
    def update(self):
        self.rect.move_ip(self.speed,0)
        if self.rect.right>1000:
            self.kill()
        pass
                
