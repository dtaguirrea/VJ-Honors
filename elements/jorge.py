"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL, K_w, K_a, K_s, K_d)


JorgePNG = pygame.image.load("assets/JorgeVJ.png")
JorgePNG_scaled = BUGpng_scaled = pygame.transform.scale(JorgePNG,(80,90))

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,player):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        self.surf=JorgePNG_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screenwidth= SCREEN_WIDTH
        self.screenheight= SCREEN_HEIGHT
        self.player=player
        pass

    def update(self, pressed_keys):
        if self.player==1:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-4)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,4)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(4,0)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-4,0)
            if self.rect.left<0:
                self.rect.left=0
            if self.rect.right>self.screenwidth:
                self.rect.right=self.screenwidth
            if self.rect.top<0:
                self.rect.top=0
            if self.rect.bottom>self.screenheight:
                self.rect.bottom=self.screenheight
            pass
        if self.player==2:
            if pressed_keys[K_w]:
                self.rect.move_ip(0,-4)
            if pressed_keys[K_s]:
                self.rect.move_ip(0,4)
            if pressed_keys[K_d]:
                self.rect.move_ip(4,0)
            if pressed_keys[K_a]:
                self.rect.move_ip(-4,0)
            if self.rect.left<0:
                self.rect.left=0
            if self.rect.right>self.screenwidth:
                self.rect.right=self.screenwidth
            if self.rect.top<0:
                self.rect.top=0
            if self.rect.bottom>self.screenheight:
                self.rect.bottom=self.screenheight
            pass
