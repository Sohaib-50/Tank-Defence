import pygame
from bullet import Bullet
import os

pygame.init()
pygame.font.init()
WINDOW = pygame.display.set_mode((600, 600))

CANNON_BULLET = pygame.image.load(os.path.join('assets', 'Heavy_Shell.png'))
CANNON_BULLET = pygame.transform.smoothscale(CANNON_BULLET, (int(CANNON_BULLET.get_width()*0.3), int(CANNON_BULLET.get_height()*0.3)))  # scale down to 70 percent of original
# vullet = Bullet((20, 20), CANNON_BULLET)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
        WINDOW.fill((244, 244,0))

        # vullet.draw(WINDOW)