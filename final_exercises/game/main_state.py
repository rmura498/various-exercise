from state import StateZero


class Character:

    def __init__(self):
        self.state = StateZero()
        self.energy = 0
        self.n_fights = 0
        #self.publisher= Publisher()

    def fight(self, another):
        increment_n_fights = 1
        self.n_fights += increment_n_fights
        another.n_fights += increment_n_fights
        self.state.fight(self, another)

    def set_state(self, new_state):
        self.state = new_state

    def lose_energy(self, energy):
        self.energy -= energy

    def gain_energy(self, energy):
        self.energy += energy


# client

ch1 = Character()
ch2 = Character()

for i in range(10):
    ch1.fight(ch2)
    print("FIGHT \n")
    print('Character 1: \n '
          'energy ->', ch1.energy,
          "\nNumber of fights", ch1.n_fights,
          "\nState - >", ch1.state)


