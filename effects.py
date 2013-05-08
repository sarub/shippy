class Effect:
    #Stats
    remaining_time = 0.0

    def applyEffect(self, ship):
        """
        Applies effects to ship
        """
        pass
    
    def tick(self, ship, time):
        """
        Applies effects and update remaining time. 
        Removes itself if exhausted
        """
        if self.remaining_time > 0:
            self.applyEffect(ship)
            self.remaining_time -= time 
        else:
            ship.effects.remove(self)
