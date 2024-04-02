import pygame

# Codigo con ayuda de Coding With Russ: https://www.youtube.com/watch?v=G8MYGDf_9ho&ab_channel=CodingWithRuss (1)
#                                       https://www.youtube.com/watch?v=2iyx8_elcYg&t=70s&ab_channel=CodingWithRuss (2)

class Button(): #Crea un boton en pantalla (1)
    def __init__(self,x,y,image, scale, screen):
        self.width = image.get_width()
        self.height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale)))
        self.og_image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y-(self.height)//2)
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


def draw_text(text, font, text_col, x, y,screen): #Función para escribir texto en pantalla (2)
        img = font.render(text, True, text_col)
        width = img.get_width()
        height = img.get_height()
        screen.blit(img, (x-(width)//2, y-(height)//2))

def cronometer_format(time,font): #Convierte tiempo en milisegundos a un formato mm:ss.ms
    cronometer_time = str(time)
    time_sec = int(time)//1000
    cronometer_minute = "00"
    cronometer_second = "00"
    if time_sec >= 1:
        if time_sec >= 60:
            cronometer_minute = "0"*(2-len(str(time_sec//60))) + str(time_sec//60)
        else:
            cronometer_minute = "00"
        if time_sec - 60 * int(cronometer_minute) >= 10:
            cronometer_second = f"{time_sec - 60 * int(cronometer_minute)}"
        else:
            cronometer_second = f"0{time_sec - 60 * int(cronometer_minute)}"
    else:
        cronometer_time_zero = f"00:00.{cronometer_time[-3:-1]}"

    cronometer_time_zero = f"{cronometer_minute}:{cronometer_second}.{cronometer_time[-3:-1]}"
    return cronometer_time_zero

class Image(): #Crea un boton en pantalla (1)
    def __init__(self,x,y,image, scale, screen):
        self.width = image.get_width()
        self.height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale)))
        self.og_image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y-(self.height)//2)
        self.screen = screen
        self.clicked = False
    
    def draw(self,x_tmp,y_tmp):
        self.rect.x = x_tmp
        self.rect.y = y_tmp
        #Dibuja el boton
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_boss_bar(self,x_tmp):
        self.image = pygame.transform.scale(self.image, (x_tmp,int(self.height*self.scale)))
        #Dibuja el boton
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    

    def change_image(self,n_image): # Permite cambiar imagen del boton
        self.image = pygame.transform.scale(n_image, (int(self.width*self.scale),int(self.height*self.scale)))
        #pygame.display.flip() 