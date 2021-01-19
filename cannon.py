from bullet import Bullet
from constants import HEIGHT
from weapon import Weapon


class Cannon(Weapon):
    REDUCE = 10  # the amount by which health will reduce on each bullet hit/enemy collision/enemy going past the player

    def __init__(self, position, vel, image, bullet_image, health=100) -> None:
        super().__init__(position, vel, image, bullet_image, health)
        self.max_health = health

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def move(self, x: int) -> None:
        super().move(x, 0)  # player can only move in x direction

    def move_bullets(self, vel: int, enemies):
        '''
        moves all bullets of player up te screen by vel units,
        removes any off screen bullets,
        removes any bullet that collides with an enemy tank and also removes the hit tank
        '''
        self.cooldown()
        for bullet in set(self.bullets):  # need to iterate over copy of bullets because the set changes during iteration
            bullet.move(vel)  # move the bullet
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            else:
                # check if the current bullet has collided with any of the enemies on screen
                for enemy in set(enemies):  # need to iterate over copy of enemies because the set changes during iteration
                    if bullet.collision(enemy):
                        enemies.remove(enemy)
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)

    def shoot(self):
        """
        adds a bullet to the list of bullets shot by the player
        """
        if self.cooldown_counter == 0:  # if player can shoot
            # keeping the starting position of bullet to be the top tip of player cannon
            bullet = Bullet((self.x+7, self.y-25), self.bullet_image)
            self.bullets.add(bullet)
            self.cooldown_counter = 1  # start cooldown

    def reduce_health(self) -> None:
        self.health -= self.REDUCE  # reduce
        