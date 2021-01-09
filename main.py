import pygame
import os
from constants import WIDTH, HEIGHT


pygame.font.init()
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Defence")


## Load images
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bgwar2.jpg")), (WIDTH, HEIGHT))  # Background image


def main_menu():
    run = True
    menu_title_font = pygame.font.SysFont("comicsans", 70)
    menu_title_label = menu_title_font.render("Press the mouse to begin...", 1, (255,255,255))

    while run:
        WINDOW.blit(BG, (0, 0))  # place the background image
        WINDOW.blit(menu_title_label, (WIDTH/2 - menu_title_label.get_width()/2, 350))  # place menu font
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main_menu()

# import pygame
# import os
# from random import randint
# from constants import WHITE, WIDTH, HEIGHT
# from helpers import update_window
# # from helper import main_menu

# def update_window(window, background):
#     window.blit(background, (20, 20))
    

# def main():

#     pygame.init()
#     WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Tank Defence")

#     BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bgwar2.jpg")), (WIDTH, HEIGHT))  # Background Image
#     # BG = pygame.image.load(os.path.join("assets", "bgwar2.jpg"))  # Background Image
#     clock = pygame.time.Clock()  # to mantain frame rate
#     FPS = 60  # Frame rate

#     run = True
#     while run:
#         clock.tick(FPS)
#         update_window(WINDOW, BG)
#         WINDOW.fill(WHITE)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

# if __name__ == "__main__":
#     main()

