from util import *
from ships import *

class Projectile(object):
    range = 9999
    speed = 10.0
    direction = 180
    position = None
    owner = None
    image = None
    image_file = "art/projectile.png"
    damage = 0.0

    def __init__(self, ship, origin, direction, damage):
        """
        Inits the projectile from a ship
        """
        self.position = origin
        self.owner = ship
        self.direction = direction
        self.image = pygame.image.load(self.image_file).convert()
        self.damage = damage

    def tick(self):
        """
        Updates the projectile
        """
        self.position = self.position.getNewPosition(self.direction, self.speed)
        #Check for offscreen
        if self.position.x <= 0 or self.position.x > SCREEN_WIDTH or self.position.y <= 0 or self.position.y > SCREEN_HEIGHT:
            self.owner.projectiles.remove(self)

    def collision(self, ship):
        """
        Manages the collision with other object
        """
        ship.impact(self)

        self.owner.projectiles.remove(self)

class Bomb(Projectile):
    range = 100
    speed = 1.0
    image_file = "art/projectile.png"


