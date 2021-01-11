from pygame import mask
from bullet import Bullet
from constants import HEIGHT

class Weapon:
    COOLDOWN = 25

    def __init__(self, position, vel, image, bullet_image, health=100) -> None:
        assert len(position) == 2  # must be x, y cooridinate pair

        self.x = position[0]
        self.y = position[1]
        self.image = image
        self.mask = mask.from_surface(self.image)
        self.bullet_image = bullet_image
        self.bullets = []
        self.vel = vel
        self.cooldown_counter = 0
        self.health = health


    def draw(self, window) -> None:
        window.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)
            

    def get_width(self):
        return self.image.get_width()


    def get_height(self):
        return self.image.get_height()

    def move(self, x, y):
        self.x += x
        self.y += y

    
    def get_health(self):
        return self.health
    
    def cooldown(self):
        '''
        adjusts cooldown counter value
        '''
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0 
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

