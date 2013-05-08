from generators import *
from shields import *
from weapons import *
from util import Position

class Ship:
    #Stats
    speed = 1.0
    
    hull = 40.0

    #Weapons
    weapon_main = Weapon()
    weapon_sec = Weapon()

    #Accesories
    generator = Generator()
    shield = Shield()
    
    #Active effects
    effects = []

    #Current position
    position = None

    #Spammed projectiles
    projectiles = []

    def __init__(self, position):
        self.position = position

    def fireWeapon(self, weapon):
        """
        Fires a weapon
        Returns false if unable to fire
        """
        return weapon.fire(self)

    def toggleFireMode(self):
        """
        Toggles secondary weapon mode
        """
        self.weapon_sec.toggleMode()

    def tick(self, time):
        """
            Updates accesories and effects status
        """
        for effect in self.effects:
            effect.tick(self, time)

        self.weapon_main.tick(self, time)
        self.weapon_sec.tick(self, time)
        self.generator.tick(self, time)
        self.shield.tick(self, time)

    def consume(self, cost):
        """
        Consumes an amount of energy
        Returns false if unable
        """
        if self.generator.energy >= cost:
            self.generator.energy -= cost
            return True
        else:
            return False

    def impact(self, damage):
        """
        Calculates remaining shield and hull after a hit
        Hull gets twice the damage after shields absortion
        """
        self.shield.energy -= damage
        if self.shield.energy < 0:
            self.hull -= -1 * (self.shield.energy * 2)
            self.shield.energy = 0.0

    def move(self, direction):
        """
        Moves the ship to a new position
        """
        self.position = self.position.getNewPosition(direction, self.speed)
      
