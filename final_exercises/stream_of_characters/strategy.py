from abc import ABC, abstractmethod


class Strategy(ABC):

    @staticmethod
    @abstractmethod
    def print_character(character):
        pass


class StrategyLower(Strategy):

    @staticmethod
    def print_character(character):
        return character.lower()


class StrategyUpper(Strategy):

    @staticmethod
    def print_character(character):
        return character.upper()
