from abc import ABC, abstractmethod


class State(ABC):

    def __str__(self):
        return self.__class__.__name__

    def fight(self, ch1, ch2):
        self._action(ch1, ch2)
        self._change_state(ch1)

    @abstractmethod
    def _action(self, ch1, ch2):
        pass

    @abstractmethod
    def _change_state(self, ch1):
        pass


class StateZero(State):

    def _action(self, ch1, ch2):
        energy = 1
        ch1.gain_energy(energy)
        ch2.lose_energy(energy)

    def _change_state(self, ch1):
        if ch1.energy > 3:
            ch1.set_state(StateOne())


class StateOne(State):

    def _action(self, ch1, ch2):
        energy_gained = 2
        energy_loss = 1
        ch1.gain_energy(energy_gained)
        ch2.lose_energy(energy_loss)

    def _change_state(self, ch1):
        if ch1.n_fights > 3:
            ch1.set_state(StateTwo())


class StateTwo(State):

    def _action(self, ch1, ch2):
        energy_gained = 3
        energy_loss = 2
        ch1.gain_energy(energy_gained)
        ch2.lose_energy(energy_loss)

    def _change_state(self, ch1):
        if ch1.energy > 10:
            ch1.set_state(StateThree())


class StateThree(State):

    def _action(self, ch1, ch2):
        energy_gained = 3
        energy_loss = 2
        ch1.gain_energy(energy_gained)
        ch2.lose_energy(energy_loss)

    def _change_state(self, ch1):
        pass
