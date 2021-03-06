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
    
    #Active effects
    effects = []

    #Current position
    position = None

    score = 0

    def __init__(self, position, level):
        self.position = position
        self.image = pygame.image.load("art/ship_1.png").convert()
        self.level = level
        self.weapon_main = Weapon(self)
        self.weapon_sec = SideWeapon(self)
        self.generator = Generator()
        self.shield = Shield()

    def fireWeapon(self, weapon):
        """
        Fires a weapon
        Returns false if unable to fire
        """
        return weapon.fire()

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

        self.weapon_main.tick()
        self.weapon_sec.tick()
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

    def impact(self, damage, owner = None):
        """
        Calculates remaining shield and hull after a hit
        Hull gets twice the damage after shields absortion
        """
        self.shield.energy -= damage
        if self.shield.energy < 0.0:
            self.hull += (self.shield.energy)
            self.shield.energy = 0.0

    def move(self, direction, speed=None):
        """
        Moves the ship to a new position
        """
        if speed is None:
            speed = self.speed

        self.position = self.position.getNewPosition(direction, speed)
        
        #Check screen boundaries
        if self.position.x > SCREEN_WIDTH - self.image.get_width():
            self.position.x = SCREEN_WIDTH - self.image.get_width()
        elif self.position.x < 0:
            self.position.x = 0

        if self.position.y > SCREEN_HEIGHT - self.image.get_height():
            self.position.y = SCREEN_HEIGHT - self.image.get_height()
        elif self.position.y < 0:
            self.position.y = 0
      
