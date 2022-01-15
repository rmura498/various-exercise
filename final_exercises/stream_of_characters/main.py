from state import *

"""
Pattern:

(state, input) -> output, next state

(lower, lower) -> upper, upper
(lower, upper) -> lower, lower
(upper, lower) -> upper, upper
(upper, upper) -> lower, lower

"""


# context
class PrintCharacter:

    def __init__(self, init_state=StateLower()):
        self.state = init_state

    def f(self, el):
        self.state.process_input(self, el)

    def set_state(self, new_state):
        self.state = new_state

    def print_element(self, character):
        print(str(self.state), '->', character)


obj = PrintCharacter()

list_of_el = ['a', 'A', 'A', 'a', 'a', 'a', 'A', 'A', 'A', 'a', 'A']
for el in list_of_el:
    obj.f(el)
