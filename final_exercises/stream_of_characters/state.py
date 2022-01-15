from abc import ABC, abstractmethod


class State(ABC):

    def __str__(self):
        return self.__class__.__name__

    def process_input(self, print_character, el):
        self._action(print_character, el)
        self._change_state(print_character, el)

    @abstractmethod
    def _action(self, print_character, el):
        pass

    @abstractmethod
    def _change_state(self, print_character, el):
        pass


class StateLower(State):

    def _action(self, print_character, el):
        if el.isupper():
            print_character.print_element(el.lower())
        else:
            print_character.print_element(el.upper())

    def _change_state(self, print_character, el):
        if el.islower():
            print_character.set_state(StateUpper())


class StateUpper(State):

    def _action(self, print_character, el):
        if el.islower():
            print_character.print_element(el.upper())
        else:
            print_character.print_element(el.lower())

    def _change_state(self, print_character, el):
        if el.isupper():
            print_character.set_state(StateLower())
