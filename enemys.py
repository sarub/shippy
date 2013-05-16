from util import *
from ships import Ship
from generators import *
from weapons import *

class Enemy(Ship):    
    hull = 125.0
    value = 1

    def __init__(self, position, level):
        self.position = position
        self.level = level
        self.image = pygame.image.load("art/ship_1.png").convert()
        self.generator = Generator()
        self.shield = Shield()
        self.weapon_main = BackWeapon(self)
        self.weapon_sec = Weapon(self)

    def tick(self):
        super(Enemy, self).tick()
        self.move(0)
        self.fireWeapon(self.weapon_main)

    def move(self, direction):
        """
        Moves the ship to a new position
        """
        self.position = self.position.getNewPosition(direction, self.speed)
        
        #Check screen boundaries
        if self.position.x > SCREEN_WIDTH \
            or self.position.x < 0 \
            or self.position.y > SCREEN_HEIGHT \
            or self.position.y < 0:
            self.level.spammed_enemys.remove(self)

    def impact(self, damage, owner=None):
        self.hull -= damage

        if self.hull <= 0.0:
            try:
                self.level.spammed_enemys.remove(self)
            except:
                pass

            if owner is not None:
                owner.score += self.value
