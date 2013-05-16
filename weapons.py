from projectiles import *

class Weapon:
    #Stats
    cost = 4.0
    time_between_shots = 2.0
    
    #Alternate mode stats
    alt_cost = 7.5
    alt_time_between_shots = 2.0

    remaining_time = 0.0
    firing = False
    alt_mode = False
    
    def __init__(self, owner):
        self.owner = owner

    def tick(self):
        """
        Updates remaining time to next shot
        """
        if self.firing:
            self.remaining_time -= 1
            if self.remaining_time <= 0:
                self.firing = False
                self.remaining_time = 0.0

    def fire(self):
        """
        Fires the weapon
        Returns false if unable
        """
        if not self.firing:
            if self.alt_mode:
                cost = self.alt_cost
                time_between_shots = self.alt_time_between_shots
            else:
                cost = self.cost
                time_between_shots = self.time_between_shots 

            if self.owner.consume(cost):
                self.remaining_time = time_between_shots
                self.firing = True
                self.createProjectiles()
                    
                return True
        else:
            return False
        
    def toggleMode(self):
        """
        Toggles fire mode
        """
        self.alt_mode = not self.alt_mode

    def createProjectiles(self):
        """
        Spams new projectiles
        """
        projectile = Projectile(self.owner, Position(self.owner.position.x + self.owner.image.get_width() / 2, self.owner.position.y), 180, 10.0)
        self.owner.level.projectiles.append(projectile)

class BackWeapon(Weapon):
    cost = 4.0
    time_between_shots = 20.0
    remaining_time = 0.0
    firing = False
    alt_mode = False

    def createProjectiles(self):
        """
        Spams new projectiles
        """
        self.owner.level.projectiles.append(Projectile(self.owner, Position(self.owner.position.x, self.owner.position.y + self.owner.image.get_height()), 340, 20.0, 5))
        self.owner.level.projectiles.append(Projectile(self.owner, Position(self.owner.position.x + self.owner.image.get_width(), self.owner.position.y + self.owner.image.get_height()), 20, 20.0, 5))

class SideWeapon(Weapon):
    cost = 15
    time_between_shots = 20.0
    remaining_time = 0.0
    firing = False
    alt_mode = False

    def createProjectiles(self):
        """
        Spams new projectiles
        """
        self.owner.level.projectiles.append(Projectile(self.owner, Position(self.owner.position.x, self.owner.position.y), 225, 20.0))
        self.owner.level.projectiles.append(Projectile(self.owner, Position(self.owner.position.x + self.owner.image.get_width(), self.owner.position.y), 135, 20.0))

