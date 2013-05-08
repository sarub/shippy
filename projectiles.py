from util import Position

class Projectile:
    tipe = None
    damage = 0.0
    range = 9999
    speed = 1.0
    direction = 0
    position = None
    origin = None

    def __init__(self, ship):
        """
        Inits the projectile from a ship
        """
        self.position = ship.position.getNewPosition(self.direction, self.speed)
        self.origin = ship

    def tick(self, time):
        """
        Updates the projectile
        """
        self.position = self.position.getNewPosition(self.direction, self.speed * time)

    def collision(self, object):
        """
        Manages the collision with other object
        """
        if isinstance(object, Ship):
            object.impact(damage)
