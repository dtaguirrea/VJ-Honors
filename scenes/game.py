'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame, time
import random
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT, K_p, K_1,K_2,K_b,K_v,K_n,K_m,K_j,K_k,K_e,K_SPACE)

from elements.jorge import Player

from elements.bug import (Enemy,Boss,Boss_Missile,Boss_Ray,Boss_Ball)

from elements.buttons import (Button, draw_text,cronometer_format,Image)

from elements.bullet import Bullet

from elements.powerup import Powerup

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
    background_image = pygame.image.load("assets/background_image_3.jpg").convert()
    background_image_scaled = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    #movimiento
    velocidad_screen=0
    FPS=20
    pause_menu_image = pygame.image.load("assets/pause_background.jpg").convert()
    pause_menu_image_scaled = pygame.transform.scale(pause_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    menu_image = pygame.image.load("assets/menu_background.jpg").convert()
    menu_image_scaled = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    select_player_menu_image = pygame.image.load("assets/select_player_background.jpg").convert()
    select_player_menu_image_scaled = pygame.transform.scale(select_player_menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    game_over_image = pygame.image.load("assets/game_over_background.jpg").convert()
    game_over_image_scaled = pygame.transform.scale(game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    win_image = pygame.image.load("assets/win_background.jpg").convert()
    win_image_scaled = pygame.transform.scale(win_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    font = pygame.font.Font('assets/minecraft.ttf', 32)
    
    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''
    
    clock = pygame.time.Clock()
    
    ''' 1.- creamos la instancia de jugador'''
    #player1 = Player(SCREEN_WIDTH,SCREEN_HEIGHT,1)
    #player2 = Player(SCREEN_WIDTH,SCREEN_HEIGHT,2)
    player_qty = 0

    #Puntuacion:
    puntuacion = 0
    record_puntuacion = 0

    ''' 3.- generador de enemigos y powerups'''
    
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY,600 - puntuacion//10)
    
    ADDPOWERUP = pygame.USEREVENT + 5
    pygame.time.set_timer(ADDPOWERUP,6000+puntuacion*4)
    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    players = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    powerups =pygame.sprite.Group()
    enemy_attacks = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    #players.add(player1)
    #players.add(player2)
    all_sprites = pygame.sprite.Group()
    #all_sprites.add(players)

    '''Creacion boss'''
    boss_bar_image = pygame.image.load("assets/boss_bar.png").convert_alpha()
    boss_bar = Image(SCREEN_WIDTH//2,100,boss_bar_image,1,screen)
    boss_bar_border_image = pygame.image.load("assets/boss_bar_border.png").convert_alpha()
    boss_bar_border = Image(SCREEN_WIDTH//2,100,boss_bar_border_image,1,screen) 
    boss_state = 0
    
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

    powerupcronometer_time1 = ""
    powerupcronometer1 = font.render(powerupcronometer_time1,True,(255,255,255),None)
    powerupcronometer_time2 = ""
    powerupcronometer2 = font.render(powerupcronometer_time2,True,(255,255,255),None)

    """Sonidos"""
    sonido_bala=pygame.mixer.Sound("Sonido/Sonido_pato.wav")
    #sonido_bala.set_volume(ruido)
    #cosas necesarias
    modo_play=False
    modo_menu=False
    modo_pausa=False
    modo_over=False
    modo__bosstest=False
    pygame.mixer.music.load("Sonido/Musica_menu2.mp3")
    pygame.mixer.music.play(-1) 
    
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
    #Estados del modo de juego: "main", "boss"
    play_state = "main"


    #Variables para el boss:
    boss_alive = False
    boss_attack_cycle = 0
    boss_appear_counter = 0
    ADDENEMY_BOSS_FIGHT = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDENEMY_BOSS_FIGHT,2000 - puntuacion//2)
    #Aparicion
    alert_boss_image_1 = pygame.image.load("assets/boss_alert_1.png").convert_alpha()
    alert_boss_image_scaled_1 = pygame.transform.scale(alert_boss_image_1, (SCREEN_WIDTH, 500))
    alert_boss_1 = Image(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,alert_boss_image_scaled_1,1,screen)
    alert_boss_image_2 = pygame.image.load("assets/boss_alert_2.png").convert_alpha()
    alert_boss_image_scaled_2 = pygame.transform.scale(alert_boss_image_2, (SCREEN_WIDTH, 500))
    alert_boss_2 = Image(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,alert_boss_image_scaled_2,1,screen)
    alert_boss_image_3 = pygame.image.load("assets/boss_alert_3.png").convert_alpha()
    alert_boss_image_scaled_3 = pygame.transform.scale(alert_boss_image_3, (SCREEN_WIDTH, 500))
    alert_boss_3 = Image(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,alert_boss_image_scaled_3,1,screen)
    #Misiles
    missile_alive = False
    ADDBOSS_MISSILE = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDBOSS_MISSILE,4000)
    #Rayo
    color_counter = 100
    color_up = True
    warning_bar_image = pygame.image.load("assets/Danger_warning.png").convert_alpha()
    warning_bar_image_scaled = pygame.transform.scale(warning_bar_image, (SCREEN_WIDTH, 500))
    warning_bar = Image(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,warning_bar_image_scaled,1,screen)
    new_boss_ray = 0
    #Bolas
    ADDBOSS_BALLS = pygame.USEREVENT + 4
    pygame.time.set_timer(ADDBOSS_BALLS,3500)
    balls_alive = False
    #Target
    player_target_image = pygame.image.load("assets/player_target.png").convert_alpha()
    player_target_image_2 = pygame.image.load("assets/player_target_2.png").convert_alpha()
    player_target = Image(0,0,player_target_image,0.13,screen)
    boss_state_1_counter = 0

    #estado inicial
    estado_inicial=0
    while running == True:
        # Actualizar la posición del fondo
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p or event.key == K_ESCAPE :
                    if game_state == "pause":
                        game_state = "play"
                    elif game_state == "play":
                        game_state = "pause"
                    else:
                        pass
                if event.key == K_SPACE and game_state=="play" and player1.cooldown==0:
                    new_bullet = Bullet(player1.rect.right,player1.rect.top,SCREEN_WIDTH,SCREEN_HEIGHT)
                    bullets.add(new_bullet)
                    if player1.powerup=="ammo":
                        player1.cooldown=1
                    if player1.powerup!="ammo":
                        player1.cooldown=20
                    all_sprites.add(new_bullet)
                    player1.abre=True
                    player1.cambio_imagen()
                    sonido_bala.play()
                elif game_state=="play":
                    player1.abre=False
                    player1.cambio_imagen()
                if event.key == K_e and game_state=="play" and player_qty==2 and player2.cooldown==0:
                    new_bullet = Bullet(player2.rect.right,player2.rect.top,SCREEN_WIDTH,SCREEN_HEIGHT)
                    bullets.add(new_bullet)
                    if player2.powerup=="ammo":
                        player2.cooldown=1
                    if player2.powerup!="ammo":
                        player2.cooldown=20
                    all_sprites.add(new_bullet)
                    
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY and game_state == "play" and play_state == "main":
                new_enemy = Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDPOWERUP and game_state == "play":
                if random.randint(0,10)<=8:
                    new_powerup = Powerup(SCREEN_WIDTH,SCREEN_HEIGHT,random.randint(0,8))
                    powerups.add(new_powerup)
                    all_sprites.add(new_powerup)
            elif event.type == ADDENEMY_BOSS_FIGHT and game_state == "play" and play_state == "boss":
                new_enemy = Enemy(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDBOSS_MISSILE and game_state == "play" and play_state == "boss" and boss_state == 1:
                missile_alive = True
                new_boss_misile = Boss_Missile(SCREEN_WIDTH,SCREEN_HEIGHT)
                enemy_attacks.add(new_boss_misile)
                all_enemies.add(new_boss_misile)
                all_sprites.add(new_boss_misile)
            elif event.type == ADDBOSS_BALLS and game_state == "play" and play_state == "boss" and boss_state == 3:
                balls_alive = True
                for i in range(1,6):
                    new_boss_ball = Boss_Ball(SCREEN_WIDTH,SCREEN_HEIGHT,boss,i)
                    enemy_attacks.add(new_boss_ball)
                    all_enemies.add(new_boss_ball)
                    all_sprites.add(new_boss_ball)
        
        #Reloj para los ataques del boss
    
        if 400 < boss_attack_cycle < 1000:
            boss_state = 1
            balls_alive = False
        elif 1250 < boss_attack_cycle < 1300:
            missile_alive = False
        elif 1300 < boss_attack_cycle < 1500:
            boss_state = 4
        elif 1500 < boss_attack_cycle < 1700:
            boss_state = 2
            if boss_attack_cycle == 1501:
                new_boss_ray = Boss_Ray(SCREEN_WIDTH,SCREEN_HEIGHT,boss)
                enemy_attacks.add(new_boss_ray)
                all_enemies.add(new_boss_ray)
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
            if estado_inicial==0:
                player1.escudo=False
                player1.abre=False
            estado_inicial+=1
            if player1.powerup=="shield":
                player1.escudo=True
                player1.cambio_imagen()
            else:
                player1.escudo=False
                player1.cambio_imagen()
            #sonido
            modo_play=True
            modo_menu=False
            modo_pausa=False
            modo_over=False
            modo__bosstest=False
            #movimiento pantalla
            screen_moviendose=velocidad_screen%background_image_scaled.get_rect().width
            screen.blit(background_image_scaled, (screen_moviendose-background_image_scaled.get_rect().width, 0))
            velocidad_screen-=FPS
            if screen_moviendose<SCREEN_WIDTH:
                screen.blit(background_image_scaled, (screen_moviendose,0))

            for player in players:
                collision = pygame.sprite.spritecollideany(player, all_enemies)
                if collision:
                    if player.powerup != "shield":
                        game_state = "over"
                        for player in players:
                            player.powerup = None
                            player.poweruptimer=0
                    else:
                        collision.kill()
                        player.powerup = "none"
                        player.poweruptimer=0
            if player1.powerup=="explotion":
                for enemy in enemies:
                    enemy.kill()
                    puntuacion+=1
                    player1.poweruptimer=0
                player1.powerup=None
            if player_qty == 2:
                player2.update(pressed_keys)
                # if pygame.sprite.spritecollideany(player2,enemies) or pygame.sprite.spritecollideany(player2,enemy_attacks) or pygame.sprite.spritecollideany(player2,bosses):
                #     if player2.powerup!="shield":
                #         player2.powerup=None
                #         game_state = "over"
                #     else:
                #         pygame.sprite.spritecollideany(player2,enemies).kill()
                if player2.powerup=="explotion":
                    for enemy in enemies:
                        enemy.kill()
                        puntuacion+=1
                        player2.poweruptimer=0
                    player2.powerup=None
            for enemy in enemies:
                collision = pygame.sprite.spritecollideany(enemy,bullets)
                if collision:
                    puntuacion += 1
                    enemy.kill()
                    if player1.powerup!="piercing":
                        collision.kill()
                    if player_qty==2:
                        if player2.powerup!="piercing":
                            collision.kill()
            for powerup in powerups:
                collision=pygame.sprite.spritecollideany(powerup,players)
                if collision:
                    if powerup.type==0 or powerup.type==1:
                        collision.powerup="speed"
                    if powerup.type==2 or powerup.type==3:
                        collision.powerup="ammo"
                    if powerup.type==4 or powerup.type==5:
                        collision.powerup="shield"
                    if powerup.type==6:
                        collision.powerup="explotion"
                    if powerup.type==7 or powerup.type==8:
                        collision.powerup="piercing"
                    collision.poweruptimer=300
                    powerup.kill()
            if puntuacion > 100 and boss_alive == False:
                boss_appear_counter += 1
                alert_boss_1.draw(alert_boss_1.rect.x,alert_boss_1.rect.y,200)
                alert_boss_3.draw(alert_boss_1.rect.x-boss_appear_counter,alert_boss_1.rect.y,200)
                alert_boss_2.draw(alert_boss_1.rect.x+boss_appear_counter,alert_boss_1.rect.y,240)
                if boss_appear_counter == 200:
                    play_state = "boss"
                    boss_alive = True
                    boss_attack_cycle = 0
                    boss = Boss(SCREEN_WIDTH,SCREEN_HEIGHT)
                    bosses.add(boss)
                    all_enemies.add(boss)
                    all_sprites.add(boss)

            player1.update(pressed_keys)
            enemies.update()
            bullets.update()

            if play_state == "boss":
                #
                boss_attack_cycle += 1
                boss.update()
                for entity in enemies:
                    screen.blit(entity.surf,entity.rect)
                for boss in bosses:
                    collision = pygame.sprite.spritecollideany(boss,bullets)
                    if collision:
                        boss.life -= 1
                        collision.kill()
                if boss.life == 0:
                    boss.kill()
                    game_state = "win"
                #Estados de ataques del boss
                if missile_alive == 1:
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
                if boss_state == 4:
                    if color_up:
                        color_counter += 2
                    elif color_up == False:
                        color_counter -= 2
                    if color_counter > 200:
                        color_up = False
                    elif color_counter < 100:
                        color_up = True
                    warning_bar.draw(warning_bar.rect.x,warning_bar.rect.y,color_counter)
                if boss_state == 2:
                    new_boss_ray.update(boss)
                    screen.blit(new_boss_ray.surf,new_boss_ray.rect)
                if balls_alive:
                    for entity in enemy_attacks:
                        if type(entity) == type(new_boss_ball):
                            entity.update()
                
                #
                for entity in all_sprites:
                    if entity != new_boss_ray and type(entity) != type(Enemy(0,0)):
                        screen.blit(entity.surf,entity.rect)
                if missile_alive == 1:
                    player_target.draw(player1.rect.x,player1.rect.y,255)
                boss_bar.draw_boss_bar(boss_bar.width*(boss.life/100))
                boss_bar_border.draw(boss_bar_border.rect.x,boss_bar_border.rect.y,255)
                pass

            if play_state == "main":
                for entity in all_sprites:
                    screen.blit(entity.surf,entity.rect)
            clock.tick(40)
    
            #CRONOMETRO EN PANTALLA
            game_time_int = pygame.time.get_ticks() - out_time_int - old_time_int
            cronometer_time = cronometer_format(game_time_int,font)
            cronometer = font.render(cronometer_time, True, (255,255, 255), None)
            screen.blit(cronometer, cronometer_Rect)

            powerupcronometer_time1=cronometer_format(player1.poweruptimer*10,font)[4:]
            #El cronometro funciona con milisegundos, asique si el tiempo está en segundos agregale un *1000
            powerupcronometer1 = font.render(powerupcronometer_time1,True, (255,255,255),None)
            powerupcronometer1_rect=powerupcronometer1.get_rect()
            powerupcronometer1_rect.center=(player1.rect.centerx,player1.rect.centery-60)
            if player1.powerup!=None and player1.powerup != "none":
                screen.blit(powerupcronometer1,powerupcronometer1_rect)
            if player_qty ==2:
                powerupcronometer_time2=cronometer_format(player2.poweruptimer*10,font) [4:]
                powerupcronometer2_rect=powerupcronometer2.get_rect()
                powerupcronometer2_rect.center=(player2.rect.centerx,player2.rect.centery-60)
                #El cronometro funciona con milisegundos, asique si el tiempo está en segundos agregale un *1000
                powerupcronometer2 = font.render(powerupcronometer_time2,True, (255,255,255),None)
                if player2.powerup!=None and player1.powerup != "none":
                    screen.blit(powerupcronometer2,powerupcronometer2_rect)
            #Puntuacion en pantalla
            draw_text(f"Puntuacion = {str(puntuacion)}",font,(255,255,255),150-len(str(puntuacion)), SCREEN_HEIGHT-30,screen)
        
        elif game_state == "menu": #MENU DE INICIO
            #sonido
            inicio_debe_sonar_algo=False
            modo_play=False
            modo_menu=True
            modo_pausa=False
            modo_over=False
            modo__bosstest=False
            # 
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
            #sonido
            modo_play=False
            modo_menu=False
            modo_pausa=True
            modo_over=False
            modo__bosstest=False
            #
            screen.blit(pause_menu_image_scaled, [0, 0])
            draw_text(f"Puntuacion: {puntuacion}",font,(255,255,255),SCREEN_WIDTH/2,150,screen)
            draw_text(f"Tiempo: {cronometer_time}",font,(255,255,255),SCREEN_WIDTH/2,200,screen)
            out_time_int = pygame.time.get_ticks() - game_time_int - old_time_int
            if button_7.draw(button_7_image_1):
                game_state = "play"
            if button_6.draw(button_6_image_1):
                game_state = "menu"
                menu_state = "main"
                play_state = "main"
                boss_alive = False
                for entity in all_sprites:
                    entity.kill()
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                player_qty = 0
                puntuacion = 0
                time.sleep(0.15)
            if button_2_1.draw(button_2_image_1):
                running = False

        elif game_state == "over":
            #sonido
            modo_play=False
            modo_menu=False
            modo_pausa=False
            modo_over=True
            modo__bosstest=False
            #
            if game_time_int > record_time_int:
                record_time_int = game_time_int
                record_str = cronometer_format(record_time_int,font)
            if puntuacion > record_puntuacion:
                record_puntuacion = puntuacion
            screen.blit(game_over_image_scaled, [0, 0])
            draw_text(f"Record: {record_str}",font,(255, 191, 0),250,300,screen)
            if game_time_int == record_time_int:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,191,0),250,350,screen)
            else:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,255,255),250,350,screen)
            draw_text(f"Record: {record_puntuacion}",font,(255, 191, 0),250,200,screen)
            if record_puntuacion == puntuacion:
                draw_text(f"Puntuacion: {puntuacion}",font,(255,191,0),250,250,screen)
            else:
                draw_text(f"Puntuacion: {puntuacion}",font,(255,255,255),250,250,screen)
            if button_1_2.draw(button_1_image_1):
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                puntuacion = 0
                game_state = "play"
                play_state = "main"
                boss_alive = False
                for entity in all_sprites:
                    if entity in enemies or entity in enemy_attacks or entity in bullets or entity in bosses or entity in powerups:
                        entity.kill()
                    elif entity in players:
                        entity.rect.move_ip(-4000,-4000)
            if button_6_2.draw(button_6_image_1):
                game_state = "menu"
                menu_state = "main"
                play_state = "main"
                boss_alive = False
                for entity in all_sprites:
                    entity.kill()
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                puntuacion = 0
                player_qty = 0
                time.sleep(0.15)
            if button_2_2.draw(button_2_image_1):
                running = False

        elif game_state == "win":
            #sonido
            modo_play=False
            modo_menu=False
            modo_pausa=False
            modo_over=False
            modo_win = True
            modo__bosstest=False
            #
            if game_time_int > record_time_int:
                record_time_int = game_time_int
                record_str = cronometer_format(record_time_int,font)
            if puntuacion > record_puntuacion:
                record_puntuacion = puntuacion
            screen.blit(win_image_scaled, [0, 0])
            draw_text(f"Record: {record_str}",font,(255, 191, 0),375,350,screen)
            if game_time_int == record_time_int:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,191,0),375,400,screen)
            else:
                draw_text(f"Tiempo: {cronometer_time}",font,(255,255,255),375,400,screen)
            draw_text(f"Record: {record_puntuacion}",font,(255, 191, 0),375,250,screen)
            if record_puntuacion == puntuacion:
                draw_text(f"Puntuacion: {puntuacion}",font,(255,191,0),375,300,screen)
            else:
                draw_text(f"Puntuacion: {puntuacion}",font,(255,255,255),375,300,screen)
            if button_1_2.draw(button_1_image_1):
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                puntuacion = 0
                game_state = "play"
                play_state = "main"
                boss_alive = False
                for entity in all_sprites:
                    if entity in enemies or entity in enemy_attacks or entity in bullets or entity in bosses or entity in powerups:
                        entity.kill()
                    elif entity in players:
                        entity.rect.move_ip(-4000,-4000)
            if button_6_2.draw(button_6_image_1):
                game_state = "menu"
                menu_state = "main"
                play_state = "main"
                boss_alive = False
                for entity in all_sprites:
                    entity.kill()
                old_time_int = pygame.time.get_ticks()
                out_time_int = 0
                game_time_int = 0
                puntuacion = 0
                player_qty = 0
                time.sleep(0.15)
            if button_2_2.draw(button_2_image_1):
                running = False
        #sonido        

        if modo_play==False and game_state=="play":
           pygame.mixer.music.load("Sonido/Musica_play_1.mp3")
           pygame.mixer.music.play(-1) 
        elif modo_menu==False and game_state=="menu":
                pygame.mixer.music.load("Sonido/Musica_menu2.mp3")
                pygame.mixer.music.play(-1) 
        elif modo_over==False and game_state=="over":
            pygame.mixer.music.load("Sonido/Musica_over1.mp3")
            pygame.mixer.music.play(-1) 
        elif modo_pausa==False and game_state=="pause":
            pass
        elif modo__bosstest==False and game_state=="boss_test":
            pass
        
        pygame.display.flip()
                
    
