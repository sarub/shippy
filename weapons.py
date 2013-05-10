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

    def tick(self, ship, time):
        """
        Updates remaining time to next shot
        """
        if self.firing:
            self.remaining_time -= time
            if self.remaining_time <= 0:
                self.firing = False
                self.remaining_time = 0.0

    def fire(self, ship):
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

            if ship.consume(cost):
                self.remaining_time = time_between_shots
                self.firing = True
                self.createProjectiles(ship)
                    
                return True
        else:
            return False
        
    def toggleMode(self):
        """
        Toggles fire mode
        """
        self.alt_mode = not self.alt_mode

    def createProjectiles(self, ship):
        """
        Spams new projectiles
        """
        projectile = Projectile(ship, ship.position)
        ship.projectiles.append(projectile)

        projectile = Projectile(ship, Position(ship.position.x + ship.image.get_width(), ship.position.y))
        ship.projectiles.append(projectile)

