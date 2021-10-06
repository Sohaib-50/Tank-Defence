import pygame
from constants import WIDTH, HEIGHT, RED, GREEN


def get_highscore() -> int:
    '''
    gets high score from file
    '''
    with open("highscore.txt", "r") as file:
        return int(file.read())


def update_highscore(new_highscore: int) -> None:
    '''
    updates the highscore in file to the the parameter new_score
    '''
    with open("highscore.txt", "w") as file:
        file.write(str(new_highscore))


def draw_healthbar(window, player) -> None:
    '''
    draws the player's health bar on around top left of screen
    '''
    pygame.draw.rect(window, RED, (10, 45, 120, 15))
    pygame.draw.rect(window, GREEN, (10, 45, 120 * (player.health/player.max_health), 15))


def draw_track(window, track_image) -> None:
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
