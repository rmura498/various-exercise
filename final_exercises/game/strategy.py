from abc import ABC, abstractmethod


class Strategy(ABC):

    def fight(self, ch1, ch2):
        self._gain_energy(ch1)
        self._loss_energy(ch2)

    @staticmethod
    @abstractmethod
    def _gain_energy(ch):
        pass

    @staticmethod
    @abstractmethod
    def _loss_energy(ch):
        pass


class DayStrategy(Strategy):

    @staticmethod
    def _gain_energy(ch):
        energy_to_gain = 1
        ch.energy += energy_to_gain

    @staticmethod
    def _loss_energy(ch):
        energy_to_lose = 1
        ch.energy -= energy_to_lose


class NightStrategy(Strategy):

    @staticmethod
    def _gain_energy(ch):
        energy_to_gain = 2
        ch.energy += energy_to_gain

    @staticmethod
    def _loss_energy(ch):
        energy_to_lose = 1.5
        ch.energy -= energy_to_lose
