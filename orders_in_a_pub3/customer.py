class Customer:
    def __init__(self, strategy):
        self.cost = 0
        self.strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
       self._strateßgy = strategy

    def print_bill(self):
        print(self.cost)

    def add_drink(self, n, unit_cost):
        self.cost += self.strategy.compute_price(n * unit_cost)



    def get_actual_dress(self):
        self.strategy.get_actual_dress()

