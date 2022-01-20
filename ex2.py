from abc import ABC, abstractmethod


class Strategy(ABC):

    @staticmethod
    @abstractmethod
    def process_1(el):
        pass

    @staticmethod
    @abstractmethod
    def process_2(el):
        pass


class StrategyWorkingDay(Strategy):

    @staticmethod
    def process_1(el):
        print(el)

    @staticmethod
    def process_2(el):
        print(el.upper())


class StrategyWeekend(Strategy):

    @staticmethod
    def process_1(el):

        """
        mi sono reso conto tardi che nella lista il 3 è posto come '3' e non
        come numero quindi la condizione nell'else non verrà mai verificata 
        ecco perchè non è presente 'it is a number' 
        """
        if type(el) is str:
            print(el.upper())
        else:
            print(el, " -> IT IS A NUMBER! ", )

    @staticmethod
    def process_2(el):
        print(el, 'ASCII ->', ord(el))




class Printer:

    def __init__(self, strategy=StrategyWorkingDay()):
        self.strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, new_strategy):
        self._strategy = new_strategy

    def process_1(self, el):
        self.strategy.process_1(el)

    def process_2(self, el):
        self.strategy.process_2(el)


# COMPLETE THE CODE


if __name__ == '__main__':
    ## COMPLETE THE CODE!
    print("\n\n")

    p = Printer()
    elements = ['a', 'B', '3']

    print('MONDAY - FRIDAY')
    for el in elements:
        p.process_1(el)
        p.process_2(el)

    p.strategy = StrategyWeekend()

    print("\n\n")
    print('SATURDAY - SUNDAY')

    for el in elements:
        p.process_1(el)
        p.process_2(el)

"""OUTPUT:


MONDAY - FRIDAY
a
A
B
B
3
3



SATURDAY - SUNDAY
A
a  ASCII ->  97
B
B  ASCII ->  66
3  -> IT IS A NUMBER!
3  ASCII ->  51

"""


