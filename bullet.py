from pygame import mask
from helpers import collide

class Bullet():
    def __init__(self, position, img) -> None:
        self.x = position[0]
        self.y = position[1]
        self.image = img
        self.mask = mask.from_surface(self.image)


    def get_x(self) -> int:
        return self.x


    def get_y(self) -> int:
        return self.y
        

    def draw(self, window) -> None:
        window.blit(self.image, (self.x, self.y))


    def move(self, vel) -> None:
        self.y += vel

    def off_screen(self, screen_height) -> None:
        return not(self.y <= screen_height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)