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
    weapon_main = None
    weapon_sec = None

    #Accesories
    generator = None
    shield = None
    

    def fireWeapon(self, weapon):
        """
        Fires a weapon if its not on firing process and has enought energy
        """
        if not weapon.isFiring() and self.generator.energy >= weapon.getEnergyCost():
            weapon.fire()
            self.generator.energy = self.generator.energy - weapon.getEnergyCost()
            return True
        else:
            return False

    def toggleFireMode(self):
        """
        Toggles secondary weapon mode
        """
        self.weapon_sec.toggleMode()

    def tick(self):
        """
            Updates accesories status (shield and generator energy recharge and weapons firing rate)
        """
        self.weapon_main.tick()
        self.weapon_sec.tick()
        self.generator.tick()
        self.shield.tick() 

    def impact(self, power):
        """
        Calculates remaining shield and hull after a hit
        Hull gets twice the damage after shields absortion
        """
        self.shield.energy = self.shield.energy - power
        if self.shield.energy < 0:
            self.hull = self.hull - (self.shield.energy * 2)
            self.shield.energy = 0

    def getVelocity(self, direction):
        """
        Returns ship velocity for specified direction
        """
        return self.velocity[direction]
            

