from util import *

class Projectile:
    tipe = None
    damage = 0.0
    range = 9999
    speed = 10.0
    direction = 180
    position = None
    owner = None

    def __init__(self, ship, origin):
        """
        Inits the projectile from a ship
        """
        self.position = origin.getNewPosition(self.direction, self.speed)
        self.owner = ship

    def tick(self, time):
        """
        Updates the projectile
        """
        self.position = self.position.getNewPosition(self.direction, self.speed * time)
        #Check for offscreen
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH or self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.owner.projectiles.remove(self)

    def collision(self, object):
        """
        Manages the collision with other object
        """
        if isinstance(object, Ship):
            object.impact(damage)

