"""
Hola este es modulo Bug,
este modulo manejara la creacion y acciones de los Bugs
"""
import pygame
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load("assets/bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng,(60,61))
Bosspng = pygame.image.load("assets/boss.png")
Bosspng_scaled = pygame.transform.scale(Bosspng,(500,500))

class Enemy(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,type):
        # nos permite invocar métodos o atributos de Sprite
        super(Enemy, self).__init__()
        self.surf = BUGpng_scaled
        self.type=type
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.speedx = random.randint(3,5)
        self.speedy = random.randint(3,5)
        if self.type==0:
            self.rect = self.surf.get_rect(
                center=(
                    SCREEN_WIDTH + 100,
                    random.randint(0,SCREEN_HEIGHT)
                )
            )
        if self.type==1:
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(50, SCREEN_WIDTH-50),
                    random.choice([50,SCREEN_HEIGHT-50])
                )
            )
            self.speedx = random.randint(3,5)*random.choice([-1,1])
            self.speedy = random.randint(3,5)*random.choice([-1,1])
        if self.type==2:
            self.rect = self.surf.get_rect(
                center=(
                    SCREEN_WIDTH + 100,
                    random.randint(0,SCREEN_HEIGHT)
                )
            )
    
        self.swidth=SCREEN_WIDTH
        self.sheight=SCREEN_HEIGHT
        pass


    def update(self):
        if self.type==0:
            self.rect.move_ip(-self.speedx,0)
            if self.rect.right<0:
                self.kill()
        if self.type==1:
            self.rect.move_ip(-self.speedx,self.speedy)
            if self.rect.left < 0 or self.rect.right > self.swidth :
                self.speedx = -self.speedx
            if self.rect.top < 0 or self.rect.bottom > self.sheight:
                self.speedy = -self.speedy
        pass

class Boss(pygame.sprite.Sprite):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Boss, self).__init__()
        self.surf = Bosspng_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.screenwidth= SCREEN_WIDTH
        self.screenheight= SCREEN_HEIGHT
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH - 100,
                SCREEN_HEIGHT//2
            )
        )
        self.speed = 2
        self.going_up = True
        self.life = 100
        pass


    def update(self):
        if self.rect.top > 20 and self.going_up:
            self.rect.move_ip(0,-self.speed)
        else:
            self.going_up = False
        if self.rect.bottom < self.screenheight - 20 and self.going_up == False:
            self.rect.move_ip(0,self.speed)
        else:
            self.going_up = True
        pass


Boss_missile_png = pygame.image.load("assets/boss_missile.png")
Boss_Missile_png_scaled = pygame.transform.scale(Boss_missile_png,(Boss_missile_png.get_width()*2,Boss_missile_png.get_height()*2))
class Boss_Missile(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # nos permite invocar métodos o atributos de Sprite
        super(Boss_Missile, self).__init__()
        self.surf = Boss_Missile_png_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.screenwidth= SCREEN_WIDTH
        self.screenheight= SCREEN_HEIGHT
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH - 100,
                SCREEN_HEIGHT//2
            )
        )
        self.speed = 2
        pass

    def update(self,player):
        dist_x = self.rect.x - (player.rect.x + player.surf.get_width()/2) 
        dist_y = self.rect.y - (player.rect.y + player.surf.get_height()/2) 
        if dist_x < 150:
            self.rect.move_ip(-4,0)
        elif dist_y == 0:
            self.rect.move_ip(-dist_x/abs(dist_x)*4,0)
        else:
            self.rect.move_ip(-dist_x/abs(dist_x)*4,-dist_y/abs(dist_y)*4)
        if self.rect.right<0:
            self.kill()
        pass

Boss_ray_png = pygame.image.load("assets/Boss_ray.png")
Boss_ray_png_scaled = pygame.transform.scale(Boss_ray_png,(2000,Boss_ray_png.get_height()*3))
class Boss_Ray(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,boss):
        # nos permite invocar métodos o atributos de Sprite
        super(Boss_Ray, self).__init__()
        self.surf = Boss_ray_png_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.screenwidth= SCREEN_WIDTH
        self.screenheight= SCREEN_HEIGHT
        self.rect = self.surf.get_rect(
            center=(
                boss.rect.x,
                boss.rect.y + boss.surf.get_height()/2
            )
        )
        self.speed = 2
        pass
    def update(self,boss):
        self.rect = self.surf.get_rect(
            center=(
                boss.rect.x,
                boss.rect.y + boss.surf.get_height()/2
            )
        )
Boss_ball_png = pygame.image.load("assets/Boss_ball.png")
Boss_ball_png_scaled = pygame.transform.scale(Boss_ball_png,(80,80))
class Boss_Ball(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,boss,number):
        # nos permite invocar métodos o atributos de Sprite
        super(Boss_Ball, self).__init__()
        self.surf = Boss_ball_png_scaled
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.screenwidth= SCREEN_WIDTH
        self.screenheight= SCREEN_HEIGHT
        self.rect = self.surf.get_rect(
            center=(
                boss.rect.x,
                boss.rect.y + boss.surf.get_height()/2
            )
        )
        self.speed = 5
        self.number = number
        pass
    def update(self):
        if self.number == 1:
            self.rect.move_ip(-self.speed+0.5,-self.speed)
        elif self.number == 2:
            self.rect.move_ip(-self.speed-0.5,-self.speed+1.5)
        elif self.number == 3:
            self.rect.move_ip(-self.speed-1,0)
        elif self.number == 4:
            self.rect.move_ip(-self.speed-0.5,self.speed-1.5)
        elif self.number == 5:
            self.rect.move_ip(-self.speed+0.5,self.speed)
            
        if self.rect.right<0:
                self.kill()
        pass