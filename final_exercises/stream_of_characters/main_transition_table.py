class PrintCharacter:

    def __init__(self, init_state=0):
        self.state = init_state
        self.transition_table = {

            0: {  # state zero
                True: {'action': self._print_upper, 'next_state': 1},
                False: {'action': self._print_lower, 'next_state': 0}
            },
            1: {  # state zero
                False: {'action': self._print_upper, 'next_state': 1},
                True: {'action': self._print_lower, 'next_state': 0}
            }

        }

    @staticmethod
    def _print_upper(el):
        print(el.upper())

    @staticmethod
    def _print_lower(el):
        print(el.lower())


    def f(self, el):
        dict_action_state = self._retrieve_action_state(el)
        self._action(dict_action_state, el)
        self._state_transition(dict_action_state)

    def _retrieve_action_state(self, el):
        dict_actual_state = self.transition_table[self.state]
        if self.state == 0:
            if el.isupper():
                return dict_actual_state[False]
            else:
                return dict_actual_state[True]
        elif self.state == 1:
            if el.islower():
                return dict_actual_state[False]
            else:
                return dict_actual_state[True]

    @staticmethod
    def _action(dict_action_state, el):
        dict_action_state['action'](el)

    def _state_transition(self, dict_action_state):
        self.state = dict_action_state['next_state']


obj = PrintCharacter()

list_of_el = ['a', 'A', 'A', 'a', 'a', 'a', 'A', 'A', 'A', 'a', 'A']
for el in list_of_el:
    obj.f(el)
