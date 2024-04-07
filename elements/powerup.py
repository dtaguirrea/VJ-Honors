"""
Hola este es modulo powerup,
este modulo manejara la creacion y acciones de los powerups
"""
import pygame
import random
from pygame.locals import (RLEACCEL)
Speedpng = pygame.image.load("assets/speed.png")
Speedpng_scaled = pygame.transform.scale(Speedpng,(60,60))
Shieldpng = pygame.image.load("assets/shield.png")
Shieldpng_scaled = pygame.transform.scale(Shieldpng,(60,60))
Explotionpng = pygame.image.load("assets/explotion.png")
Explotionpng_scaled = pygame.transform.scale(Explotionpng,(60,60))
Piercingpng = pygame.image.load("assets/piercing.png")
Piercingpng_scaled = pygame.transform.scale(Piercingpng,(60,60))
Ammopng = pygame.image.load("assets/ammo.png")
Ammopng_scaled = pygame.transform.scale(Ammopng,(60,60))
class Powerup (pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,type):
        super(Powerup, self).__init__()
        self.type=type
        if type==0 or type==1:
            self.surf = Speedpng_scaled
        elif type==2 or type==3:
            self.surf = Ammopng_scaled
        elif type==4 or type==5:
            self.surf = Shieldpng_scaled
        elif type==6:
            self.surf = Explotionpng_scaled
        elif type==7 or type ==8:
            self.surf = Piercingpng_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(50,SCREEN_WIDTH-50),
                random.randint(50,SCREEN_HEIGHT-50)
            )
        )
        pass
    def update(self):
        pass