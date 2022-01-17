from state import StateZero
from publisher_ex2_game import Publisher


class Character:

    def __init__(self):
        self.state = StateZero()
        self.energy = 0
        self.n_fights = 0
        self.publisher = Publisher(['state_one', 'change_state'])

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
