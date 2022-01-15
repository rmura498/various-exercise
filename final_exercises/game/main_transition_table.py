class CharactersFighting:
    energy_needed = 3
    n_fights_needed = 3

    def change_energy(self, energy_gain, energy_loss, another):
        self.energy += energy_gain
        another.energy -= energy_loss

    def __init__(self, start_state=0):
        self.state = start_state
        self.energy = 0
        self.n_fights = 0
        self.transition_table = {
            0: {  # state zero
                CharactersFighting.energy_needed: {'action': self.change_energy, 'next_state': 1},
                'default_input': {'action': self.change_energy, 'next_state': 0}
            },
            1: {  # state one
                CharactersFighting.n_fights_needed: {'action': self.change_energy, 'next_state': 2},
                'default_input': {'action': self.change_energy, 'next_state': 1}
            },
            2: {  # state two

                'default_input': {'action': self.change_energy, 'next_state': 2}
            }

        }

    def fight(self, another):
        self.n_fights += 1
        dict_action_state = self._retrieve_action_state(another)
        self.action(dict_action_state, another)
        self.state_transition(dict_action_state)

    def _retrieve_action_state(self, another):
        dict_actual_state = self.transition_table[self.state]
        default_action_state = dict_actual_state['default_input']
        if self.state == 0:
            dict_action_state = dict_actual_state.get(self.energy, default_action_state)
            return dict_action_state
        elif self.state == 1:
            dict_action_state = dict_actual_state.get(self.n_fights, default_action_state)
            return dict_action_state
        else:
            return default_action_state

    def state_transition(self, dict_action_state):
        self.state = dict_action_state['next_state']

    def action(self, dict_action_state, another):
        if self.state == 0:
            energy_gain = 1
            energy_loss = 1
            dict_action_state['action'](energy_gain, energy_loss, another)
        elif self.state == 1:
            energy_gain = 2
            energy_loss = 1
            dict_action_state['action'](energy_gain, energy_loss, another)
        elif self.state == 2:
            energy_gain = 3
            energy_loss = 2
            dict_action_state['action'](energy_gain, energy_loss, another)


ch1 = CharactersFighting()
ch2 = CharactersFighting()

for i in range(6):
    ch1.fight(ch2)
    print("\nFIGHT \n")
    print('Character 1: \n '
          'energy ->', ch1.energy,
          "\nNumber of fights", ch1.n_fights,
          "\nState - >", ch1.state, '\n')
"""    print('Character 2: \n '
          'energy ->', ch2.energy,
          "\nNumber of fights", ch2.n_fights,
          "\nState - >", ch2.state,'\n')
"""
