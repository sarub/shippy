from generators import *
from shields import *
from weapons import *
from util import *
import pygame


class Ship(object):
    #Stats
    image = None
    speed = 4.0
    
    max_hull = 40.0
    hull = 40.0

    #Weapons
    weapon_main = Weapon()
    weapon_sec = SideWeapon()

    #Accesories
    generator = Generator()
    shield = Shield()
    
    #Active effects
    effects = []

    #Current position
    position = None

    #Spammed projectiles
    projectiles = []

    score = 0

    def __init__(self, position):
        self.position = position
        self.image = pygame.image.load("art/ship_1.png").convert()

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

    def tick(self):
        """
            Updates accesories and effects status
        """
        for effect in self.effects:
            effect.tick(self)

        for projectile in self.projectiles:
            projectile.tick()

        self.weapon_main.tick(self)
        self.weapon_sec.tick(self)
        self.generator.tick(self)
        self.shield.tick(self)

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
        if self.shield.energy < 0.0:
            self.hull += (self.shield.energy)
            self.shield.energy = 0.0

    def move(self, direction):
        """
        Moves the ship to a new position
        """
        self.position = self.position.getNewPosition(direction, self.speed)
        
        #Check screen boundaries
        if self.position.x > SCREEN_WIDTH - self.image.get_width():
            self.position.x = SCREEN_WIDTH - self.image.get_width()
        elif self.position.x < 0:
            self.position.x = 0

        if self.position.y > SCREEN_HEIGHT - self.image.get_height():
            self.position.y = SCREEN_HEIGHT - self.image.get_height()
        elif self.position.y < 0:
            self.position.y = 0
      
