"""
Hola este es modulo Jorge,
este modulo manejara la creacion y movimiento de Jorge
"""
import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL, K_w, K_a, K_s, K_d)


JorgePNG = pygame.image.load("assets/JorgeVJ.png")
JorgePNG_scaled = pygame.transform.scale(JorgePNG,(80,90))
#probando la apertura
JorgePNG_abierto= pygame.image.load("assets/JorgeVJabierto.png")
JorgePNG_abierto_scaled=pygame.transform.scale(JorgePNG_abierto,(80,90))

JorgePNG_2 = pygame.image.load("assets/JorgeVJ2.png")
JorgePNG_scaled_2 = pygame.transform.scale(JorgePNG_2,(80,90))

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,player):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        if player == 1:
            self.surf=JorgePNG_scaled
        elif player == 2:
            self.surf=JorgePNG_scaled_2
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screenwidth= SCREEN_WIDTH
        self.screenheight= SCREEN_HEIGHT
        self.player=player
        self.cooldown=0
        self.powerup=None
        self.poweruptimer=0
        self.speed=4
        pass
    #probando la apertura
    def cambio_imagen(self):
        if self.abre:
            self.surf = JorgePNG_abierto_scaled
        else:
            self.surf = JorgePNG_scaled
    def update(self, pressed_keys):
        if self.player==1:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-self.speed)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,self.speed)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.speed,0)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-self.speed,0)
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
        if self.powerup=="speed":
            self.speed=8
        if self.powerup==None:
            self.speed=4
        if self.poweruptimer>0 and self.powerup!=None:
            self.poweruptimer=self.poweruptimer-1
            if self.poweruptimer==0:
                self.powerup=None
        if self.cooldown >0:
            self.cooldown=self.cooldown-1
        pass
