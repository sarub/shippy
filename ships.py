from generators import *
from shields import *
from weapons import *

class Ship:
    #Constants
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    #Stats
    velocity = [1.0, 1.0, 1.0, 1.0] #Up, right, down, left    
    hull = 40.0

    #Weapons
    weapon_main = Weapon()
    weapon_sec = Weapon()

    #Accesories
    generator = Generator()
    shield = Shield()
    
    effects = []

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

    def impact(self, power):
        """
        Calculates remaining shield and hull after a hit
        Hull gets twice the damage after shields absortion
        """
        self.shield.energy -= power
        if self.shield.energy < 0:
            self.hull -= -1 * (self.shield.energy * 2)
            self.shield.energy = 0.0

    def getVelocity(self, direction):
        """
        Returns ship velocity for specified direction
        """
        return self.velocity[direction]
      
