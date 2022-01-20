class Customer(object):

    def __init__(self):
        self.tot_cost = 0
        self.dress = "Normal dress"

    @staticmethod
    def _compute_bill(drink, cost, happy_hour):
        if not happy_hour:
            return drink * cost
        else:
            return drink * cost * 0.5

    def add_drink(self, drink, cost, happy_hour=False):
        bill = self._compute_bill(drink, cost, happy_hour)
        self.tot_cost += bill

    def get_actual_dress(self, happy_hour=False):
        if not happy_hour:
            self.dress = "Normal"
            return self.dress
        else:
            self.dress = "Happy Hour"
            return self.dress


customer1 = Customer()
customer1.add_drink(1, 7)  # 1 drink, 7 euros for each drink
print(customer1.tot_cost)
print(customer1.get_actual_dress())


customer1.add_drink(1, 7, happy_hour=True)  # 1 drink, 7 euros for each drink
print(customer1.tot_cost)

print(customer1.get_actual_dress( happy_hour=True))
