import os
from random import choice, randint
from sys import exit
from typing import Set

import pygame

from cannon import Cannon
from constants import (BLACK, BULLETS_VEL, ENEMY_VEL, FPS, GREEN, GREY, HEIGHT,
                       PLAYER_VEL, WAVE_INCREMENT, WHITE, WIDTH)
from helpers import collide, draw_healthbar, draw_track, get_highscore, update_highscore
from tank import Tank


pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Defence")
CLOCK = pygame.time.Clock()  # to limit framerate


## Load images
BG = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))  # Background image

TRACK = pygame.image.load(os.path.join('assets', 'track.png'))  # player's tracks
TRACK = pygame.transform.smoothscale(TRACK, (int(TRACK.get_width()*0.5), int(TRACK.get_height()*0.5)))  # scale down to 50 percent of original
TRACK = pygame.transform.rotate(TRACK, 90)  # rotate by 90 degrees

CANNON_IMG = pygame.image.load(os.path.join('assets', 'cannon.png'))
CANNON_IMG = pygame.transform.smoothscale(CANNON_IMG, (int(CANNON_IMG.get_width()*0.6), int(CANNON_IMG.get_height()*0.6)))  # scale down to 60 percent of original

TANK_IMG_1 = pygame.image.load(os.path.join("assets", "tank1.png"))
TANK_IMG_1 = pygame.transform.smoothscale(TANK_IMG_1, (int(TANK_IMG_1.get_width()*0.45), int(TANK_IMG_1.get_height()*0.45))) # scale down to 45 percent of original

TANK_IMG_2 = pygame.image.load(os.path.join("assets", "tank2.png"))
TANK_IMG_2 = pygame.transform.smoothscale(TANK_IMG_2, (int(TANK_IMG_2.get_width()*0.50), int(TANK_IMG_2.get_height()*0.50))) # scale down to 50 percent of original

CANNON_BULLET = pygame.image.load(os.path.join('assets', 'cannon_shell.png'))
CANNON_BULLET = pygame.transform.smoothscale(CANNON_BULLET, (int(CANNON_BULLET.get_width()*0.7), int(CANNON_BULLET.get_height()*0.7)))  # scale down to 70 percent of original

TANK_BULLET = pygame.image.load(os.path.join('assets', 'tank_shell.png'))
TANK_BULLET = pygame.transform.smoothscale(TANK_BULLET, (int(TANK_BULLET.get_width()*0.80), int(TANK_BULLET.get_height()*0.80)))  # scale down to 80 percent of original
TANK_BULLET = pygame.transform.rotate(TANK_BULLET, 180)


def play() -> None:
    '''
    contains main game logic
    '''
    run = True
    lost = False
    highscore = get_highscore()  # read highscore from file
    stats_font = pygame.font.Font(os.path.join("assets", "arial.ttf"), 25)  # for level and health texts
    game_over_font = pygame.font.Font(os.path.join("assets", "impact.ttf"), 80)
    level = 0
    lost_time = 0
    enemies: Set[Tank] = set()  # set of enemies currently alive
    wave_size = 0  # number of enemies in a level
    player_cannon = Cannon(position=(WIDTH/2 - CANNON_IMG.get_width()/2, HEIGHT*0.81),
                            vel=PLAYER_VEL, image=CANNON_IMG, bullet_image=CANNON_BULLET)


    def update_window() -> None:
        '''
        updates the window to show the latest state of the game
        '''
        level_label = stats_font.render(f"Current Level: {level}", 1, WHITE)
        highscore_label = stats_font.render(f"Best: {max(highscore, level)}", 1, WHITE)
        health_label = stats_font.render(f"Health", 1, WHITE)
        
        WINDOW.blit(BG, (0, 0))  # background image
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))  # level text
        WINDOW.blit(highscore_label, (WIDTH - highscore_label.get_width() - 10, 45))
        WINDOW.blit(health_label, (10, 10))  # health text
        draw_healthbar(WINDOW, player_cannon)
        draw_track(WINDOW, TRACK)  # cannon track
        for enemy in enemies:  # draw enemies
            enemy.draw(WINDOW) 
        player_cannon.draw(WINDOW)  # cannon
    
        if lost:
            lost_label = game_over_font.render("Game Over.", 1, WHITE)
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, HEIGHT*1/5))  # You lost message
            if level > highscore:
                new_highscore_label = game_over_font.render(f"NEW HIGHSCORE: {level}!!!", 1, WHITE)
                WINDOW.blit(new_highscore_label, (WIDTH/2 - new_highscore_label.get_width()/2, HEIGHT*1/2))  # You lost message

        pygame.display.update()  # make the latest changes appear on screen


    while run:
        CLOCK.tick(FPS)  # to mantain framerate
        update_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if cross button clicked or alt+f4 pressed
                pygame.quit()  # close pygame
                exit()  # exit the program

        if player_cannon.get_health() <= 0:
            lost = True
            lost_time += 1

        if lost:
            if lost_time > (FPS * 3):  # if lost for 3 seconds 
                run = False
                if level > highscore:
                    update_highscore(level)
            else:
                continue  # to show the lost message for 3 seconds and not do any more changes in the game

        if len(enemies) == 0:  # if all enemies of current level are destroyed
            level += 1
            wave_size += WAVE_INCREMENT
            # add new enemies
            for i in range(wave_size):
                x = randint(
                    max(0, player_cannon.get_x()-WIDTH//3),
                    min(WIDTH-TANK_IMG_1.get_width(), player_cannon.get_x()+((WIDTH*2)//3))
                    )  # to make new enemies spawn more towards the area player is currently in
                y = randint(-HEIGHT, -HEIGHT//4)  
                new_enemy = Tank(position=(x, y), vel=ENEMY_VEL, image=choice((TANK_IMG_1, TANK_IMG_2)), bullet_image=TANK_BULLET)
                enemies.add(new_enemy)

        keys_pressed = pygame.key.get_pressed()  # get all keys that are currently pressed

        # keys for moving left/right
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            if player_cannon.get_x() + player_cannon.get_width() + PLAYER_VEL <= WIDTH:  # check for right edge
                player_cannon.move(PLAYER_VEL)  # move right by PLAYER_VEL units
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            if player_cannon.get_x() - PLAYER_VEL >= 0:  # check for left edge
                player_cannon.move(-PLAYER_VEL)  # move left by PLAYER_VEL units

        # Key for shooting
        if keys_pressed[pygame.K_SPACE]:
            player_cannon.shoot()

        for enemy in set(enemies):  # need to iterate over copy of enemies because the set changes during iteration
            enemy.move()
            enemy.move_bullets(BULLETS_VEL, player_cannon)

            if collide(enemy, player_cannon) or enemy.get_y() > HEIGHT:  # collide with player or offscreen
                player_cannon.reduce_health()  # TODO: health or lives?
                enemies.remove(enemy)
                
            # make enemies shoot at random times
            if randint(0, FPS*2) == 1:
                enemy.shoot()


        player_cannon.move_bullets(-BULLETS_VEL, enemies)
    


def main_menu() -> None:
    BTN_PADDING = 10
    run = True
    menu_font_1 = pygame.font.Font(os.path.join("assets", "comic.ttf"), 100)
    menu_font_2 = pygame.font.Font(os.path.join("assets", "arialbd.ttf"), 35)
    menu_font_3 = pygame.font.Font(os.path.join("assets", "arialbi.ttf"), 23)

    title_label = menu_font_1.render("Tank Defence", 1, WHITE)

    instructions_1 = "Instructions: You are being attacked by tanks."
    instructions_2 = "Move your cannon using 'a' and 'd' keys or right and left arrow keys."
    instructions_3 = "Press spacebar to shoot."
    instructions_4 = "You will have to shoot down all enemies in a level to move to the next level."
    instructions_5 = "You will lose health every time a bullet hits you, an opponent tank collides "
    instructions_6 = "with you or opponent tank goes past you. The game gets over when your health"
    instructions_7 = "becomes zero (health bar will be displayed on top left of screen when you start the game)."
    instructions_label_1 = menu_font_3.render(instructions_1, 1, WHITE)
    instructions_label_2 = menu_font_3.render(instructions_2, 1, WHITE)
    instructions_label_3 = menu_font_3.render(instructions_3, 1, WHITE)
    instructions_label_4 = menu_font_3.render(instructions_4, 1, WHITE)
    instructions_label_5 = menu_font_3.render(instructions_5, 1, WHITE)
    instructions_label_6 = menu_font_3.render(instructions_6, 1, WHITE)
    instructions_label_7 = menu_font_3.render(instructions_7, 1, WHITE)

    begin_label = menu_font_2.render("Play", 1, BLACK)
    begin_button = begin_label.get_rect()
    begin_button.x = WIDTH/2 - begin_label.get_width()/2 - BTN_PADDING
    begin_button.y = HEIGHT*(5/6) - BTN_PADDING
    begin_button.width += BTN_PADDING * 2
    begin_button.height += BTN_PADDING * 2

    
    while run:
        WINDOW.fill(GREY)

        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT*(1/10)))  # draw game title text
        
        # draw instructions text
        WINDOW.blit(instructions_label_1, (WIDTH/2 - instructions_label_1.get_width()/2, HEIGHT*(2/5)))
        WINDOW.blit(instructions_label_2, (WIDTH/2 - instructions_label_2.get_width()/2, HEIGHT*(2/5)+instructions_label_1.get_height()))
        WINDOW.blit(instructions_label_3, (WIDTH/2 - instructions_label_3.get_width()/2, HEIGHT*(2/5)+instructions_label_1.get_height()*2))
        WINDOW.blit(instructions_label_4, (WIDTH/2 - instructions_label_4.get_width()/2, HEIGHT*(2/5)+instructions_label_1.get_height()*3))
        WINDOW.blit(instructions_label_5, (WIDTH/2 - instructions_label_5.get_width()/2, HEIGHT*(2/5)+instructions_label_1.get_height()*5))
        WINDOW.blit(instructions_label_6, (WIDTH/2 - instructions_label_6.get_width()/2, HEIGHT*(2/5)+instructions_label_1.get_height()*6))
        WINDOW.blit(instructions_label_7, (WIDTH/2 - instructions_label_7.get_width()/2, HEIGHT*(2/5)+instructions_label_1.get_height()*7))

        pygame.draw.rect(WINDOW, GREEN, begin_button, border_radius=10)  # draw play button
        WINDOW.blit(begin_label, (WIDTH/2 - begin_label.get_width()/2, HEIGHT*(5/6)))  # draw play button text on button

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if cross button clicked or alt+f4 pressed
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # if mouse pressed
                if begin_button.collidepoint(event.pos):  # if mouse pressed on button
                    play()  # start the game

    pygame.quit()
    exit()



main_menu()
