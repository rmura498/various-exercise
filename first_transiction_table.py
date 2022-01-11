# transition_table = {
#     (state_0, input_0): {action: action, next_state: next_state},
#     (state_0, input_1): {action: action, next_state: next_state},
#     ...
#     (state_n, input_k): {action: action, next_state: next_state},
# }
#
# transition_table = {
#     state_0: {
#         input_0: {action: action, next_state: next_state},
#         input_1: {action: action, next_state: next_state},
#         default_input: {action: action, next_state: next_state}
#     },
#     state_1: {
#         input_0: {action: action, next_state: next_state},
#         input_1: {action: action, next_state: next_state},
#         default_input: {action: action, next_state: next_state}
#     }
# }


class SkipWithState_a:
    def f_null(self, v):
        pass

    def f_sum(self, v):
        self.sum_val += v

    def __init__(self, val_to_skip, start_state=0):
        self.sum_val = 0
        self.id_state = start_state
        self.transition_table = {
            0: {  # state 0
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_sum, 'next_state': 0},
            },
            1: {  # state 1
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_null, 'next_state': 0}
            }
        }

    def process_input(self, v_input):
        dict_actual_state = self.transition_table[self.id_state]

        default_action_state = dict_actual_state['default_input']

        dict_action_state = dict_actual_state.get(v_input, default_action_state)
        action = dict_action_state['action']
        next_state = dict_action_state['next_state']

        action(v_input)
        self.id_state = next_state


"""
We can improve the design.
The method process_input is responsible for both
the state transition and the action.

We can apply the single responsibility principle by writing two different methods,
state_transition() and action()

"""


class SkipWithState_b:

    def f_null(self, v):
        pass

    def f_sum(self, v):
        self.sum_val += v

    def __init__(self, val_to_skip, start_state=0):
        self.sum_val = 0
        self.id_state = start_state
        self.transition_table = {
            0: {  # state 0
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_sum, 'next_state': 0},
            },
            1: {  # state 1
                val_to_skip: {'action': self.f_null, 'next_state': 1},
                'default_input': {'action': self.f_null, 'next_state': 0}
            }
        }

    def process_input(self, v_input):
        dict_action_state = self._retrieve_action_state(v_input)
        self.action(dict_action_state, v_input)
        self.state_transition(dict_action_state)

        # ATTENTION - in this code, the correct sub-dictionary in the state transition table
        # is retrieved by _retrieve_action_state(),
        # and therefore the order in which methods .action() and .state_transition() are called does not matter.
        #
        # If you call directl
        # ----> table[self.state][input]['action']()
        # and
        # ----> self.state = table[self.state][input][''next_state'']
        # you should be careful about the order of 'perform the action' and 'change state'

    def _retrieve_action_state(self, v_input):
        dict_actual_state = self.transition_table[self.id_state]
        default_action_state = dict_actual_state['default_input']
        dict_action_state = dict_actual_state.get(v_input, default_action_state)
        return dict_action_state

    def state_transition(self, dict_action_state):
        self.id_state = dict_action_state['next_state']

    def action(self, dict_action_state, v_input):
        dict_action_state['action'](v_input)


nums1 = [1, 13, 10, 1, 13, 13, 13, 10, 1, 13]
nums2 = [1, 13, 10, 1, 13, 13, 13, 10, 1]
nums3 = [13, 10, 1, 13, 13, 13, 10, 1]

list_of_nums = [nums1, nums2, nums3]
list_of_results = [3, 3, 2]

for nums, r in zip(list_of_nums, list_of_results):
    obj = SkipWithState_a(13)

    for el in nums:
        obj.process_input(el)

    print(obj.sum_val == r)
