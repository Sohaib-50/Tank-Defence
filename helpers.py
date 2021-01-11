import pygame

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
        pygame.draw.rect(window, (255,0,0), (10, 45, 120, 15))
        pygame.draw.rect(window, (0,255,0), (10, 45, 120 * (player.health/player.max_health), 15))


def collide(obj1, obj2) -> bool:
    '''
    returns True if the two objects passed as arguments are colliding,
    False otherwise
    '''
    offset_x = int(obj2.get_x() - obj1.get_x())
    offset_y = int(obj2.get_y() - obj1.get_y())
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None