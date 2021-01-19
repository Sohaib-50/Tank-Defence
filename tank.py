from bullet import Bullet
from weapon import Weapon
from constants import HEIGHT
from cannon import Cannon


class Tank(Weapon):

    def __init__(self, position, vel, image, bullet_image) -> None:
        super().__init__(position, vel, image, bullet_image)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def move(self) -> None:
        super().move(0, self.vel)

    def move_bullets(self, vel: int, player: Cannon)  -> None:
        self.cooldown()
        for bullet in set(self.bullets): # need to iterate over copy of bullets because the set changes during iteration
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            elif bullet.collision(player):
                player.reduce_health()
                if bullet in self.bullets:
                    self.bullets.remove(bullet)
            bullet.move(vel)


    def shoot(self) -> None:
        '''
        adds a bullet to the list of bullets shot by the player
        '''
        if self.cooldown_counter == 0:  # if weapon can shoot
            bullet = Bullet((self.x+10, self.y+self.get_height()-5), self.bullet_image)
            self.bullets.add(bullet)
            self.cooldown_counter = 1  # start cooldown