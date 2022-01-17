from character import Character
from publisher_ex2_game import SubscriberStateOne, SubscriberChangeState, Publisher

# client

ch1 = Character()
ch2 = Character()


sub1 = SubscriberStateOne('sub_state_one')
sub2 = SubscriberChangeState('sub_change_state')

ch1.publisher.register(sub1, 'state_one', sub1.subscriber_method)
ch1.publisher.register(sub2, 'change_state', sub2.subscriber_method)

for i in range(10):
    ch1.fight(ch2)
    print("FIGHT \n")
    print('Character 1: \n '
          'energy ->', ch1.energy,
          "\nNumber of fights", ch1.n_fights,
          "\nState - >", ch1.state)
