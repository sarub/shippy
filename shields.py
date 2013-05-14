class Shield:
    #Stats
    max_capacity = 100.0
    energy = 100.0
    rate = 5.0
    cost = 10.0

    def tick(self, ship):
        """
        Recharges shields if generator can supply energy
        """
        if self.energy < self.max_capacity:
            if ship.consume(self.cost):
                self.energy += self.rate
            
