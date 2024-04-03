'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame, time

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_p, K_1,K_2,K_b,K_v,K_n,K_m,K_j,K_k)

from elements.jorge import Player

from elements.bug import (Enemy,Boss,Boss_Missile,Boss_Ray,Boss_Ball)

from elements.buttons import (Button, draw_text,cronometer_format,Image)


def StartScene():
    ''' iniciamos los modulos de pygame'''
    
    pygame.init()
    
    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1024  
    SCREEN_HEIGHT = 768  
    
    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    surface = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()
    background_image_scaled = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pause_menu_image = pygame.image.load("assets/pause_background.jpg").convert()
    pause_menu_image_scaled = pygame.transform.scale(pause_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    menu_image = pygame.image.load("assets/menu_background.jpg").convert()
    menu_image_scaled = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    select_player_menu_image = pygame.image.load("assets/select_player_background.jpg").convert()
    select_player_menu_image_scaled = pygame.transform.scale(select_player_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    game_over_image = pygame.image.load("assets/game_over_background.jpg").convert()
    game_over_image_scaled = pygame.transform.scale(game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
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
    enemy_attacks = pygame.sprite.Group()
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
    button_1 = Button(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,button_1_image,0.4,screen)
    button_1_1 = Button(SCREEN_WIDTH/2,400,button_1_image,0.4,screen)
    button_1_2 = Button(SCREEN_WIDTH/2+200,400,button_1_image,0.4,screen)
    #Boton "Salir"
    button_2_image = pygame.image.load("assets/Button_2.png").convert_alpha()
    button_2_image_1 = pygame.image.load("assets/Button_2_1.png").convert_alpha()
    button_2 = Button(SCREEN_WIDTH/2,SCREEN_HEIGHT/4 + SCREEN_HEIGHT/2,button_2_image,0.4,screen)
    button_2_1 = Button(SCREEN_WIDTH/2,700,button_2_image,0.4,screen)
    button_2_2 = Button(SCREEN_WIDTH/2 + 200,700,button_2_image,0.4,screen)
    #Boton "1 jugador"
    button_3_image = pygame.image.load("assets/Button_3.png").convert_alpha()
    button_3_image_1 = pygame.image.load("assets/Button_3_1.png").convert_alpha()
    button_3 = Button(300,300,button_3_image,0.4,screen)
    #Boton "2 jugadores"
    button_4_image = pygame.image.load("assets/Button_4.png").convert_alpha()
    button_4_image_1 = pygame.image.load("assets/Button_4_1.png").convert_alpha()
    button_4 = Button(300,480,button_4_image,0.4,screen)
    #Boton atrás
    button_5_image = pygame.image.load("assets/Button_5.png").convert_alpha()
    button_5_image_1 = pygame.image.load("assets/Button_5_1.png").convert_alpha()
    button_5 = Button(300,700,button_5_image,0.35,screen)
    #Boton menú
    button_6_image = pygame.image.load("assets/Button_6.png").convert_alpha()
    button_6_image_1 = pygame.image.load("assets/Button_6_1.png").convert_alpha()
    button_6 = Button(SCREEN_WIDTH/2,550,button_6_image,0.4,screen)
    button_6_2 = Button(SCREEN_WIDTH/2 + 200,550,button_6_image,0.4,screen)
    #Boton reanudar
    button_7_image = pygame.image.load("assets/Button_7.png").convert_alpha()
    button_7_image_1 = pygame.image.load("assets/Button_7_1.png").convert_alpha()
    button_7 = Button(SCREEN_WIDTH/2,400,button_7_image,0.4,screen)
    
    
    # Variables del juego:
    
    #Estados de juego: "menu", "play", "pause", "over"
    game_state = "menu"
    #Estados de menu de inicio: "main", "players"
    menu_state = "main"
    
    #Boss test
    boss_bar_image = pygame.image.load("assets/boss_bar.png").convert_alpha()
    boss_bar = Image(SCREEN_WIDTH//2,100,boss_bar_image,1,screen)
    missile_yes = False
    ADDBOSS_MISSILE = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDBOSS_MISSILE,4000)
    ADDENEMY_BOSS_FIGHT = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDENEMY_BOSS_FIGHT,1600)
    boss_state = 0
    #
    player_target_image = pygame.image.load("assets/player_target.png").convert_alpha()
    player_target_image_2 = pygame.image.load("assets/player_target_2.png").convert_alpha()
    player_target = Image(0,0,player_target_image,0.13,screen)
    boss_state_1_counter = 0
    new_boss_ray = 0
    #
    boss_attack_cycle = 0
    color_counter = 100
    color_up = True
    warning_bar_image = pygame.image.load("assets/Danger_warning.png").convert_alpha()
    warning_bar_image_scaled = pygame.transform.scale(warning_bar_image, (SCREEN_WIDTH, 500))
    warning_bar = Image(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,warning_bar_image_scaled,1,screen)
    ADDBOSS_BALLS = pygame.USEREVENT + 4
    pygame.time.set_timer(ADDBOSS_BALLS,3500)
    balls_alive = False

    
    while running == True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p or event.key == K_ESCAPE :
                    if game_state == "pause":
                        game_state = "play"
                    elif game_state == "play":
                        game_state = "pause"
                    else:
                        pass
                #Boss_test
                if event.key == K_b:
                    game_state = "boss_test"
                    for entity in enemies:
                        entity.kill()
                    boss = Boss(SCREEN_WIDTH,SCREEN_HEIGHT)
                    all_sprites.add(boss)
                    enemies.add(boss)
                if event.key == K_v:
                    boss.life -=1
                if event.key == K_m:
                    if boss_state != 2:
                        boss_state = 2
                        new_boss_ray = Boss_Ray(SCREEN_WIDTH,SCREEN_HEIGHT,boss)
                        #enemy_attacks.add(new_boss_ray)
                        enemy_attacks.add(new_boss_ray)
                        all_sprites.add(new_boss_ray)
                    else:
                        boss_state = 0
                        new_boss_ray.kill()
                if event.key == K_j:
                    if boss_state != 3:
                        boss_state = 3
                        for i in range(1,6):
                            new_boss_ball = Boss_Ball(SCREEN_WIDTH,SCREEN_HEIGHT,boss,i)
                            #enemy_attacks.add(new_boss_ray)
                            enemy_attacks.add(new_boss_ball)
                            all_sprites.add(new_boss_ball)
                    else:
                        boss_state = 0
                if event.key == K_n:
                    if boss_state != 1:
                        boss_state = 1
                    elif boss_state == 1:
                        boss_state = 0
                if event.key == K_k:
                    boss_state = 4
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY and game_state == "play":
                new_enemy = Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDENEMY_BOSS_FIGHT and game_state == "boss_test":
                new_enemy = Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDBOSS_MISSILE and game_state == "boss_test" and boss_state == 1:
                missile_yes = True
                new_boss_misile = Boss_Missile(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemy_attacks.add(new_boss_misile)
                all_sprites.add(new_boss_misile)
            elif event.type == ADDBOSS_BALLS and game_state == "boss_test" and boss_state == 3:
                balls_alive = True
                for i in range(1,6):
                    new_boss_ball = Boss_Ball(SCREEN_WIDTH,SCREEN_HEIGHT,boss,i)
                    enemy_attacks.add(new_boss_ball)
                    all_sprites.add(new_boss_ball)
        
        #BOSS ATTACKS
    
        if 400 < boss_attack_cycle < 1000:
            boss_state = 1
            balls_alive = False
        elif 1250 < boss_attack_cycle < 1300:
            missile_yes = False
        elif 1300 < boss_attack_cycle < 1500:
            boss_state = 4
        elif 1500 < boss_attack_cycle < 1700:
            boss_state = 2
            if boss_attack_cycle == 1501:
                new_boss_ray = Boss_Ray(SCREEN_WIDTH,SCREEN_HEIGHT,boss)
                enemy_attacks.add(new_boss_ray)
                all_sprites.add(new_boss_ray)
        elif 1700 < boss_attack_cycle < 1800:
            new_boss_ray.kill()
        elif 2000 < boss_attack_cycle < 2500:
            boss_state = 3
        elif boss_attack_cycle > 2600:
            boss_attack_cycle = 0
        else:
            boss_state = 0        

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
            out_time_int = pygame.time.get_ticks() - game_time_int - old_time_int
            if menu_state == "main":
                screen.blit(menu_image_scaled, [0, 0])
                if button_1.draw(button_1_image_1):
                    menu_state = "players"
                    time.sleep(0.15)
                if button_2.draw(button_2_image_1):
                    running = False
            elif menu_state == "players":
                screen.blit(select_player_menu_image_scaled, [0, 0])
                #draw_text("Menu en progreso: Presiona 1 o 2 para elegir la cantidad de jugadores",pygame.font.Font('assets/minecraft.ttf', 20),(255,255,255),SCREEN_WIDTH//2,SCREEN_HEIGHT//2,screen)
                if button_3.draw(button_3_image_1):
                    player_qty = 1
                if button_4.draw(button_4_image_1):
                    player_qty = 2
                if button_5.draw(button_5_image_1):
                    menu_state = "main"
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
            draw_text(f"Tiempo: {cronometer_time}",font,(255,255,255),SCREEN_WIDTH/2,200,screen)
            out_time_int = pygame.time.get_ticks() - game_time_int - old_time_int
            if button_7.draw(button_7_image_1):
                game_state = "play"
            if button_6.draw(button_6_image_1):
                game_state = "menu"
                menu_state = "main"
                for entity in all_sprites:
                    entity.kill()
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                player_qty = 0
            if button_2_1.draw(button_2_image_1):
                running = False

        elif game_state == "over":
            if game_time_int > record_time_int:
                record_time_int = game_time_int
                record_str = cronometer_format(record_time_int,font)
            screen.blit(game_over_image_scaled, [0, 0])
            draw_text(f"Record: {record_str}",font,(255, 191, 0),250,300,screen)
            if game_time_int == record_time_int:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,191,0),250,350,screen)
            else:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,255,255),250,350,screen)
            if button_1_2.draw(button_1_image_1):
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                game_state = "play"
                for entity in all_sprites:
                    if entity in enemies or entity in enemy_attacks:
                        entity.kill()
                    elif entity in players:
                        entity.rect.move_ip(-4000,-4000)
            if button_6_2.draw(button_6_image_1):
                game_state = "menu"
                menu_state = "main"
                for entity in all_sprites:
                    entity.kill()
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                player_qty = 0
                time.sleep(0.15)
            if button_2_2.draw(button_2_image_1):
                running = False
        
        elif game_state == "boss_test":
            boss_attack_cycle += 1
            screen.blit(background_image,[0,0])
            draw_text(str(boss.life),font,(255,255,255),SCREEN_WIDTH//2,20,screen)
            draw_text(f"Boss state = {str(boss_state)}",font,(255,255,255),SCREEN_WIDTH-150,20,screen)
            draw_text(f"Counter = {str(boss_attack_cycle)}",font,(255,255,255),40,40,screen)
            boss_bar.draw_boss_bar(boss_bar.width*(boss.life/100))
            if pygame.sprite.spritecollideany(player1,enemies) or pygame.sprite.spritecollideany(player1,enemy_attacks):
                # player1.kill()
                print("UNO")
                game_state = "over"
            if player_qty == 2:
                player2.update(pressed_keys)
                if pygame.sprite.spritecollideany(player2,enemies) or pygame.sprite.spritecollideany(player2,enemy_attacks):
                    # player2.kill()
                    print("DOS")
                    game_state = "over"
            for entity in enemies:
                screen.blit(entity.surf,entity.rect)
            player1.update(pressed_keys)
            enemies.update()
            boss.update()
            if boss_state == 2:
                new_boss_ray.update(boss)
                screen.blit(new_boss_ray.surf,new_boss_ray.rect)
            if boss.life <= 0:
                boss.kill()
            for entity in all_sprites:
                if entity != new_boss_ray and type(entity) != type(Enemy(0,0)):
                    screen.blit(entity.surf,entity.rect)
            if missile_yes == 1:
                player_target.draw(player1.rect.x,player1.rect.y,255)
                boss_state_1_counter += 1
                draw_text(f"Counter = {str(boss_state_1_counter)}",font,(255,255,255),0,20,screen)
                if 50 > boss_state_1_counter > 30:
                    player_target.change_image(player_target_image_2)
                if boss_state_1_counter > 50:
                    player_target.change_image(player_target_image)
                    boss_state_1_counter = 0
                for entity in enemy_attacks:
                    if type(entity) == type(new_boss_misile):
                        entity.update(player1)
                # if pygame.sprite.spritecollideany(player1,enemy_attacks):
                #     game_state = "over"
                #     print("TRES")
            if balls_alive:
                for entity in enemy_attacks:
                    if type(entity) == type(new_boss_ball):
                        entity.update()
            if boss_state == 4:
                screen.blit(surface, (0,0))
                if color_up:
                    color_counter += 2
                elif color_up == False:
                    color_counter -= 2
                if color_counter > 200:
                    color_up = False
                elif color_counter < 100:
                    color_up = True
                warning_bar.draw(warning_bar.rect.x,warning_bar.rect.y,color_counter)
                

                
            clock.tick(40)
                    
            
        
        pygame.display.flip()
                
    
