from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def compute_price(self, value):
        pass  # DO NOTHING

    @abstractmethod
    def get_actual_dress(self):
        pass  # DO NOTHING


class NormalStrategy:
    def compute_price(self, value):
        return value

    def get_actual_dress(self):
        print('normal dress')


class HappyHourStrategy:
    def compute_price(self, value):
        discount = 0.5
        return value * discount

    def get_actual_dress(self):
        print('HH dress')
