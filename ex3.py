from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def process_1(self, el):
        pass

    @abstractmethod
    def process_2(self, el):
        pass


class Strategy1(Strategy):
    def process_1(self, el):
        print(el)

    def process_2(self, el):
        print(el.upper())


class Strategy2(Strategy):
    def process_1(self, el):
        if el.isnumeric():
            print(el, ' -> IT IS A NUMBER!')
        else:
            print(el.upper())

    def process_2(self, el):
        print(el, ' ASCII -> ', ord(el))


"""
Ho implementato il publisher:
1- come se potessero esserci più eventi nonostante ce ne sia solo uno
in generale potremmo dover implementare più observer interessati ad altri eventi 
in futuro

2- come se gli observer potessero avere metodi differenti e non il solo 'update'
     da qui l'implementazione differente del metodo register del publisher

"""


class Publisher:

    def __init__(self, events):

        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def unregister(self, subscriber, event='changing_strategy'):
        del self.get_subscribers(event)[subscriber]

    def register(self, subscriber, event='changing_strategy', callback=None):
        default = 'update'
        if callback is None:
            callback = getattr(subscriber, default)
        self.get_subscribers(event)[subscriber] = callback

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


class Observer:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, '->', message)


# ---------------------------------------------------------#

class Printer:
    def __init__(self, processor=Strategy1(),
                 publisher=Publisher(['changing_strategy'])):
        self._processor = processor
        self.publisher = publisher

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, new_processor):
        self._processor = new_processor
        self.publisher.dispatch('changing_strategy', 'New Strategy!')

    def process_1(self, el):
        self.processor.process_1(el)

    def process_2(self, el):
        self.processor.process_2(el)


# COMPLETE THE CODE IF NEEDED


if __name__ == '__main__':

    print("\n\n")

    p = Printer()
    elements = ['a', 'B', '3']

    # Observers s1 and s2 are interested in strategy changes
    # HERE I'M USING THE INITIAL STRATEGY - NO CHANGES
    s_1 = Observer('s_1')
    s_2 = Observer('s_2')

    p.publisher.register(s_1)
    p.publisher.register(s_2)

    print('MONDAY - FRIDAY')
    for el in elements:
        p.process_1(el)
        p.process_2(el)

    print("\n\n")
    print('SATURDAY - SUNDAY')
    # CHANGE STRATEGY - Observers must print
    # s1 ->  New Strategy!
    # s2 ->  New Strategy!

    p.processor = Strategy2()
    for el in elements:
        p.process_1(el)
        p.process_2(el)

    # Observer s1 is no more interested in strategy changes
    p.publisher.unregister(s_1)

    print("\n\n")
    print('MONDAY - FRIDAY')

    # CHANGE STRATEGY - Observers must print

    # s2 ->  New Strategy!

    p.processor = Strategy1()

    for el in elements:
        p.process_1(el)
        p.process_2(el)

""" OUTPUT:


MONDAY - FRIDAY
a
A
B
B
3
3



SATURDAY - SUNDAY
s2 ->  New Strategy!
s1 ->  New Strategy!
A
a  ASCII ->  97
B
B  ASCII ->  66
3  -> IT IS A NUMBER!
3  ASCII ->  51



MONDAY - FRIDAY
s2 ->  New Strategy!
a
A
B
B
3
3



"""