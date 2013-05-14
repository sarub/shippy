from util import *

class Projectile:
    damage = 10.0
    range = 9999
    speed = 10.0
    direction = 180
    position = None
    owner = None

    def __init__(self, ship, origin, direction):
        """
        Inits the projectile from a ship
        """
        self.position = origin
        self.owner = ship
        self.direction = direction

    def tick(self):
        """
        Updates the projectile
        """
        self.position = self.position.getNewPosition(self.direction, self.speed)
        #Check for offscreen
        if self.position.x <= 0 or self.position.x > SCREEN_WIDTH or self.position.y <= 0 or self.position.y > SCREEN_HEIGHT:
            self.owner.projectiles.remove(self)

    def collision(self, object):
        """
        Manages the collision with other object
        """
        if isinstance(object, Ship):
            object.impact(damage)
        else:
            self.owner.projectiles.remove(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0 , 0), (self.position.x, self.position.y), 2)

class Bomb(Projectile):
    damage = 100
    range = 100
    speed = 1.0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0 , 0), (self.position.x, self.position.y), 2)

