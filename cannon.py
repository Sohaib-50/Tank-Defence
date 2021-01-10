import pygame
# from main import CANNON_IMG
from weapon import Weapon

class Cannon(Weapon):
    def __init__(self, x_coordinate: int, y_coordinate: int, image) -> None:
        super().__init__(x_coordinate, y_coordinate)
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        
    def draw(self, window):
        super().draw(window)
        self.draw_healthbar(window)

    def draw_healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.image.get_height() + 10, self.image.get_width(), 10))
        # pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.image.get_height() + 10, self.image.get_width() * (self.health/self.max_health), 10))
