import pygame
import os
from constants import WIDTH, HEIGHT
from weapon import Weapon
from cannon import Cannon


pygame.font.init()
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Defence")


## Load images
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bgwar5.png")), (WIDTH, HEIGHT))  # Background image
# BG = pygame.image.load(os.path.join("assets", "bgwar5.png"))  # Background image

CANNON_IMG = pygame.image.load(os.path.join('assets', 'Gun_01.png'))
CANNON_IMG = pygame.transform.scale(CANNON_IMG, (int(CANNON_IMG.get_width()*0.60), int(CANNON_IMG.get_height()*0.60)))
player_cannon = Cannon(WIDTH//2, HEIGHT-150, CANNON_IMG)
player_cannon2 = Cannon(WIDTH//3, HEIGHT-666, CANNON_IMG)
player_cannon3 = Cannon(WIDTH//8, HEIGHT-700, CANNON_IMG)

def main_menu():
    run = True
    menu_title_font = pygame.font.SysFont("comicsans", 70)
    menu_title_label = menu_title_font.render("Press the space-bar to begin...", 1, (0,0,0))

    while run:
        WINDOW.blit(BG, (0, 0))  # place the background image
        WINDOW.blit(menu_title_label, (WIDTH/2 - menu_title_label.get_width()/2, 350))  # place menu font
        player_cannon.draw(WINDOW)
        player_cannon3.draw(WINDOW)
        player_cannon2.draw(WINDOW)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main_menu()