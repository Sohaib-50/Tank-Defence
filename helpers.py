import pygame
from constants import WIDTH, HEIGHT, RED, GREEN


def get_highscore() -> int:
    '''
    gets high score from file
    '''
    pass


def update_highscore(new_score: int) -> None:
    '''
    updates the highscore in file to the the parameter new_score
    '''
    pass


def draw_healthbar(window, player):
    '''
    draws the player's health bar on around top left of screen
    '''
    pygame.draw.rect(window, RED, (10, 45, 120, 15))
    pygame.draw.rect(window, GREEN, (10, 45, 120 * (player.health/player.max_health), 15))


def draw_track(window, track_image):
    '''
    draws the track on which the player cannon can move
    '''
    x_coordinate = 0  # start drawing from the left

    while x_coordinate <= WIDTH:
        window.blit(track_image, (x_coordinate, HEIGHT-45))
        x_coordinate += track_image.get_width()


def collide(obj1, obj2) -> bool:
    '''
    returns True if the two objects (pygame surfaces) passed as arguments are colliding,
    False otherwise
    '''
    offset_x = int(obj2.get_x() - obj1.get_x())
    offset_y = int(obj2.get_y() - obj1.get_y())
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
