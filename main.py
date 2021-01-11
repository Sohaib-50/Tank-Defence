import pygame
import os
from random import randint
from constants import WIDTH, HEIGHT, FPS, PLAYER_VEL, ENEMY_VEL, BULLETS_VEL, BLACK
from cannon import Cannon
from tank import Tank
from helpers import collide, draw_healthbar


pygame.font.init()
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Defence")


## Load images
BG = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "bgwar6.png")), (WIDTH, HEIGHT))  # Background image

TRACK = pygame.image.load(os.path.join('assets', 'Track_1_A.png'))  # player's tracks
TRACK = pygame.transform.smoothscale(TRACK, (int(TRACK.get_width()*0.6), int(TRACK.get_height()*0.6)))  # scale down to 60 percent of original
TRACK = pygame.transform.rotate(TRACK, 90)  # rotate by 90 degrees

CANNON_IMG = pygame.image.load(os.path.join('assets', 'Gun_01.png'))
CANNON_IMG = pygame.transform.smoothscale(CANNON_IMG, (int(CANNON_IMG.get_width()*0.6), int(CANNON_IMG.get_height()*0.6)))  # scale down to 60 percent of original

TANK_IMG = pygame.image.load(os.path.join("assets", "M-6_preview.png"))
TANK_IMG = pygame.transform.smoothscale(TANK_IMG, (int(TANK_IMG.get_width()*0.45), int(TANK_IMG.get_height()*0.45))) # scale down to 45 percent of original

CANNON_BULLET = pygame.image.load(os.path.join('assets', 'Heavy_Shell.png'))
CANNON_BULLET = pygame.transform.smoothscale(CANNON_BULLET, (int(CANNON_BULLET.get_width()*0.7), int(CANNON_BULLET.get_height()*0.7)))  # scale down to 70 percent of original

TANK_BULLET = pygame.image.load(os.path.join('assets', 'Medium_Shell.png'))
TANK_BULLET = pygame.transform.rotate(TANK_BULLET, 180)

STATS_FONT = pygame.font.SysFont("comicsans", 40)
LOST_LABEL = pygame.font.SysFont("comicsans", 100).render("You Lost!!", 1, (0, 0, 0))


def play():
    run = True
    clock = pygame.time.Clock()  # to mantain framerate
    level = 0

    enemies = []
    wave_size = 5

    player_cannon = Cannon((WIDTH/2 - CANNON_IMG.get_width()/2, HEIGHT*0.78), vel=PLAYER_VEL, image=CANNON_IMG, bullet_image=CANNON_BULLET)

    lost = False
    lost_time = 0

    def update_window():
        level_label = STATS_FONT.render(f"Level: {level}", 1, BLACK)
        health_label = STATS_FONT.render(f"Health:", 1, BLACK)
        
        WINDOW.blit(BG, (0, 0))  # background image
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))  # level text
        WINDOW.blit(health_label, (10, 10))  # health text
        draw_healthbar(WINDOW, player_cannon)
        
        draw_track()  # cannon track
        for enemy in enemies:  # draw enemies
            enemy.draw(WINDOW) 
        player_cannon.draw(WINDOW)  # cannon
        
        if lost:
            WINDOW.blit(LOST_LABEL, (WIDTH/2 - LOST_LABEL.get_width()/2, 350))

        pygame.display.update()  # make the latest changes appear on screen



    while run:
        clock.tick(FPS)
        update_window()

        if player_cannon.get_health() <= 0:
            lost = True
            lost_time += 1

        if lost:
            if lost_time > (FPS * 3):  # if lost for 3 seconds
                run = False
            else:
                continue

        if len(enemies) == 0:  # if all enemies of current level are destroyed
            level += 1
            wave_size += 1
            for i in range(wave_size):
                enemy = Tank((randint(0, WIDTH-TANK_IMG.get_width()), randint(-HEIGHT, 0)), ENEMY_VEL, TANK_IMG, TANK_BULLET)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()

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

        for enemy in enemies[:]:
            enemy.move()
            enemy.move_bullets(BULLETS_VEL, player_cannon)

            if collide(enemy, player_cannon):
                player_cannon.reduce_health()
                enemies.remove(enemy)

            elif enemy.get_y() > HEIGHT:
                player_cannon.reduce_health()  #TODO: health or lives?
                enemies.remove(enemy)
                
            # make enemies shoot at random times
            if randint(0, FPS*2) == 1:
                enemy.shoot()
            

        player_cannon.move_bullets(-BULLETS_VEL, enemies)

    

def main_menu():
    run = True
    menu_title_font = pygame.font.SysFont("comicsans", 70)
    menu_title_label = menu_title_font.render("Press the space-bar to begin...", 1, (0,0,0))
    
    while run:
        WINDOW.blit(BG, (0, 0))  # place the background image
        WINDOW.blit(menu_title_label, (WIDTH/2 - menu_title_label.get_width()/2, 350))  # place menu font
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            play()

    pygame.quit()


def draw_track():
    '''draws the track on which the player cannon can move'''
    x_coordinate = 0  # start drawing from the left

    while x_coordinate <= WIDTH:
        WINDOW.blit(TRACK, (x_coordinate, HEIGHT-60))
        x_coordinate += TRACK.get_width()

main_menu()