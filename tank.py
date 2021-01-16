from bullet import Bullet
from weapon import Weapon
from constants import HEIGHT

class Tank(Weapon):

    def __init__(self, position, vel, image, bullet_image) -> None:
        super().__init__(position, vel, image, bullet_image)


    def get_x(self) -> int:
        return self.x


    def get_y(self) -> int:
        return self.y

    
    def move(self) -> None:
        super().move(0, self.vel)


    def move_bullets(self, vel, player):
        self.cooldown()
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen(HEIGHT):
                self.bullets.remove(bullet)
            elif bullet.collision(player):
                player.reduce_health()
                self.bullets.remove(bullet)

    def shoot(self):
        '''
        adds a bullet to the list of bullets shot by the player
        '''
        if self.cooldown_counter == 0:  # if weapon can shoot
            bullet = Bullet((self.x-35, self.y+self.get_height()*0.5), self.bullet_image)
            self.bullets.append(bullet)
            self.cooldown_counter = 1  # start cooldown


    def __repr__(self):
        return f"<Tank, x={self.x}, y={self.y}>"