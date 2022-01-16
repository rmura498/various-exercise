from strategy import StrategyLower, StrategyUpper


class Character:

    def __init__(self, strategy=StrategyLower()):
        self.strategy = strategy
        self.character = ''

    def f(self, character):
        self.character = self.strategy.print_character(character)

    def print_character(self):
        print(self.character)


obj = Character()
list_of_el = ['a', 'A', 'A', 'a', 'a', '', 'a', 'A', 'A', 'A', 'a', 'A']
for el in list_of_el:
    if el == '':
        obj.strategy = StrategyUpper
    obj.f(el)
    obj.print_character()
