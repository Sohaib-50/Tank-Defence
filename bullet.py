from pygame import mask
import pygame
from helpers import collide


class Bullet:
    def __init__(self, position, img) -> None:
        assert len(position) == 2, "x, y coordinate pair required for position"
        self.x = position[0]
        self.y = position[1]
        self.image = img
        self.mask = mask.from_surface(self.image)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def draw(self, window) -> None:
        # r = self.image.get_rect()
        # r.height
        # r.x, r.y = self.x, self.y
        # pygame.draw.rect(window, (255,255,255), r)
        window.blit(self.image, (self.x, self.y))

    def move(self, vel) -> None:
        self.y += vel

    def off_screen(self, screen_height) -> None:
        '''
        returns true if bullet has gone outside screen area
        '''
        return self.y >= screen_height or (self.y + self.mask.get_size()[0]*0.70) < 0

    def collision(self, obj):
        return collide(self, obj)

    def __repr__(self) -> str:
        return f"<Bullet ({self.x}, {self.y})>"