class Generator:
    #Stats
    energy = 100.0
    rate = 5.0

    def tick(self, ship, time):
        """
        Updates energy
        """
        self.energy += self.rate * time


