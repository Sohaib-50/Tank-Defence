import pygame
from main import *
import pygame
import os
import time
import random
pygame.font.init()
WIDTH, HEIGHT = 700, 700
# Dimensions in pixels
HEIGHT = 680  
WIDTH = (HEIGHT * 3) // 2  # for 3:2 aspect ratio
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

# Load images
# RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
# GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
# BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
#
# # Player player
# YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
#
# # Lasers
# RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
# GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
# BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
# YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bgwar2.jpg")), (WIDTH, HEIGHT))



def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None



def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                play()
    pygame.quit()
main_menu()

