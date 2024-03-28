'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_p, K_1,K_2)

from elements.jorge import Player

from elements.bug import Enemy

from elements.buttons import (Button, draw_text,cronometer_format)


def StartScene():
    ''' iniciamos los modulos de pygame'''
    
    pygame.init()
    
    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1024  
    SCREEN_HEIGHT = 768  
    
    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()
    background_image_scaled = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pause_menu_image = pygame.image.load("assets/pause_background.jpg").convert()
    pause_menu_image_scaled = pygame.transform.scale(pause_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    menu_image = pygame.image.load("assets/menu_background.jpg").convert()
    menu_image_scaled = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    font = pygame.font.Font('assets/minecraft.ttf', 32)
    
    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''
    
    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''
    
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY,600)
    
    ''' 3.- creamos la instancia de jugador'''
    #player1 = Player(SCREEN_WIDTH,SCREEN_HEIGHT,1)
    #player2 = Player(SCREEN_WIDTH,SCREEN_HEIGHT,2)
    player_qty = 0
    
    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()
    #players.add(player1)
    #players.add(player2)
    all_sprites = pygame.sprite.Group()
    #all_sprites.add(players)
    
    
    ''' hora de hacer el gameloop '''
    running = True
    
    #Variables cronometro
    out_time_int = 0
    game_time_int = 0
    old_time_int = 0
    record_time_int = 0
    cronometer_time = ""
    cronometer = font.render(cronometer_time, True, (255,255, 255), None)
    cronometer_Rect = cronometer.get_rect()
    cronometer_Rect.center = (SCREEN_WIDTH - 150, SCREEN_HEIGHT-30)
    
    
    '''BOTONES'''
    #Boton "Iniciar"
    button_1_image = pygame.image.load("assets/Button_1.png").convert_alpha()
    button_1_image_1 = pygame.image.load("assets/Button_1_1.png").convert_alpha()
    button_1 = Button(SCREEN_WIDTH/2 - int(button_1_image.get_width())/4 ,SCREEN_HEIGHT/4,button_1_image,0.5,screen)
    #Boton "Salir"
    button_2_image = pygame.image.load("assets/Button_2.png").convert_alpha()
    button_2_image_1 = pygame.image.load("assets/Button_2_1.png").convert_alpha()
    button_2 = Button(SCREEN_WIDTH/2 - int(button_2_image.get_width())/4 ,SCREEN_HEIGHT/4 + SCREEN_HEIGHT/2 - int(button_2_image.get_height())/2,button_2_image,0.5,screen)
    
    
    # Variables del juego:
    
    #Estados de juego: "menu", "play", "pause", "over"
    game_state = "menu"
    #Estados de menu de inicio: "main", "players"
    menu_state = "main"
    
    
    while running == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_p:
                    if game_state == "pause":
                        game_state = "play"
                    elif game_state == "play":
                        game_state = "pause"
                    else:
                        pass
                if menu_state == "players":
                    if event.key == K_1:
                        player_qty = 1
                        print("HOLI")
                    if event.key == K_2:
                        player_qty = 2
                        print("HOLI")
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY and game_state == "play":
                new_enemy = Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
        
        pressed_keys= pygame.key.get_pressed()
    
        # ESTADOS DE JUEGO:
        if game_state == "play":    #JUEGO SE EJECUTA
            screen.blit(background_image,[0,0])
            if pygame.sprite.spritecollideany(player1,enemies):
                # player1.kill()
                game_state = "over"
            if player_qty == 2:
                player2.update(pressed_keys)
                if pygame.sprite.spritecollideany(player2,enemies):
                    # player2.kill()
                    game_state = "over"
            player1.update(pressed_keys)
            enemies.update()
            for entity in all_sprites:
                screen.blit(entity.surf,entity.rect)
            clock.tick(40)
    
            #CRONOMETRO EN PANTALLA
            game_time_int = pygame.time.get_ticks() - out_time_int - old_time_int
            cronometer_time = cronometer_format(game_time_int,font)
            cronometer = font.render(cronometer_time, True, (255,255, 255), None)
            screen.blit(cronometer, cronometer_Rect)
        
        elif game_state == "menu": #MENU DE INICIO
            out_time_int = pygame.time.get_ticks() - game_time_int
            if menu_state == "main":
                screen.blit(menu_image_scaled, [0, 0])
                if button_1.draw(button_1_image_1):
                    menu_state = "players"
                if button_2.draw(button_2_image_1):
                    running = False
            elif menu_state == "players":
                screen.blit(pause_menu_image_scaled, [0, 0])
                draw_text("Menu en progreso: Presiona 1 o 2 para elegir la cantidad de jugadores",pygame.font.Font('assets/minecraft.ttf', 20),(255,255,255),100,500,screen)
                if player_qty != 0:
                    player1 = Player(SCREEN_WIDTH,SCREEN_HEIGHT,1)
                    players.add(player1)
                    if player_qty == 2:
                        player2 = Player(SCREEN_WIDTH,SCREEN_HEIGHT,2)
                        players.add(player2)
                    all_sprites.add(players)
                    game_state = "play"
                pass
    
        elif game_state == "pause": # MENU DE PAUSA
            screen.blit(pause_menu_image_scaled, [0, 0])
            out_time_int = pygame.time.get_ticks() - game_time_int - old_time_int
            if button_1.draw(button_1_image_1):
                game_state = "play"
            if button_2.draw(button_2_image_1):
                running = False

        elif game_state == "over":
            if game_time_int > record_time_int:
                record_time_int = game_time_int
                record_str = cronometer_format(record_time_int,font)
            screen.fill((0,0,0))
            draw_text(f"Record: {record_str}",font,(255, 191, 0),SCREEN_WIDTH//2-100,100,screen)
            if game_time_int == record_time_int:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,191,0),SCREEN_WIDTH//2-100,150,screen)
            else:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,255,255),SCREEN_WIDTH//2-100,150,screen)
            if button_1.draw(button_1_image_1):
                out_time_int = pygame.time.get_ticks()
                game_state = "play"
            if button_2.draw(button_2_image_1):
                running = False
            for entity in all_sprites:
                if entity in enemies:
                    entity.kill()
                elif entity in players:
                    entity.rect.move_ip(-4000,-4000)
                    
            
        
        pygame.display.flip()
                
    
