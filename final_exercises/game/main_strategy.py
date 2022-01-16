from strategy import DayStrategy, NightStrategy


class Character:

    def __init__(self, strategy=DayStrategy()):
        self.strategy = strategy
        self.energy = 0
        self.n_fights = 0

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, another_strategy):
        self._strategy = another_strategy

    def fight(self, another):
        self.strategy.fight(self, another)

    def get_actual_energy(self):
        print("Energy:", self.energy)


# ------------------------- main

day_strategy = DayStrategy()
night_strategy = NightStrategy()

ch1 = Character(day_strategy)
ch2 = Character(day_strategy)

ch1.fight(ch2)
ch1.get_actual_energy()

ch1.strategy = night_strategy

ch1.fight(ch2)
ch1.get_actual_energy()
