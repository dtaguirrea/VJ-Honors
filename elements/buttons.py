import pygame

# Codigo con ayuda de Coding With Russ: https://www.youtube.com/watch?v=G8MYGDf_9ho&ab_channel=CodingWithRuss

class Button():
    def __init__(self,x,y,image, scale, screen):
        self.width = image.get_width()
        self.height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale)))
        self.og_image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.screen = screen
        self.clicked = False
    
    def draw(self,mouse_image):
        
        action = False

        #Conseguir posición del mouse
        pos = pygame.mouse.get_pos()
        #print(pos)

        #Checkear si el mouse está encima
        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(mouse_image, (int(self.width*self.scale),int(self.height*self.scale)))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.image = self.og_image
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Dibuja el boton
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    
        return action

    def change_image(self,n_image): # Permite cambiar imagen del boton
        self.image = pygame.transform.scale(n_image, (int(self.width*self.scale),int(self.height*self.scale)))
        self.screen.blit(self.image, (self.rect.x, self.rect.y+100))
        #pygame.display.flip()  