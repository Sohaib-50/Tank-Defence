class Weapon:
    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x = x_coordinate
        self.y = y_coordinate
        self.image = None
        self.bullet_image = None
        self.bullets = []

    def draw(self, window) -> None:
        window.blit(self.image, (self.x, self.y))
        
    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()