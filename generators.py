class Generator:
    #Stats
    max_capacity = 100.0
    energy = 100.0
    rate = 0.5

    def tick(self, ship, time):
        """
        Updates energy
        """
        if self.energy < self.max_capacity:
            self.energy += self.rate * time


