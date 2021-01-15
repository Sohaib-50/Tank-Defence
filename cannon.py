import pygame
from weapon import Weapon
from constants import HEIGHT
from bullet import Bullet

class Cannon(Weapon):
    REDUCE = 10  # the amount by which health will reduce on each bullet hit / enemy collision

    def __init__(self, position, vel, image, bullet_image, health=100) -> None:
        super().__init__(position,vel, image, bullet_image, health)
        self.max_health = health


    def get_x(self) -> int:
        return self.x


    def get_y(self) -> int:
        return self.y


    def move(self, x) -> None:
        super().move(x, 0)


    def move_bullets(self, vel, enemies):
        self.cooldown()
        for bullet in self.bullets:  # for every bullet that's out
            bullet.move(vel)  # move the bullet
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            else:
                current = enemies
                while current is not None:
                    enemy = current.data
                    try:
                        if bullet.collision(enemy):
                            current.delete()
                            if bullet in self.bullets:
                                self.bullets.remove(bullet)
                    except:
                        print(enemies, enemy, current)
                    else:
                        current = current.next

    def shoot(self):
        '''
        adds a bullet to the list of bullets shot by the player
        '''
        if self.cooldown_counter == 0:  # if weapon can shoot
            bullet = Bullet((self.x-17, self.y-25), self.bullet_image)
            self.bullets.append(bullet)
            self.cooldown_counter = 1  # start cooldown


    def reduce_health(self):
        self.health -= self.REDUCE