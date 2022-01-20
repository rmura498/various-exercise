"""
Write a software that can store a time interval.
the software must provide the data structure to store the time interval and the 4 functions
set_h_min(), set_min(), get_h_min(), get_min()

The data structure ca be designed in two different ways (choose only one of them)
- it can store hours and minutes
- it can store minutes

Implement the software using only functions and dictionaries, for now.
No OOP is required

Key point: the interface must not change if you change the implementation
If the implementation changes, the main will work correctly without changes
"""


def create_time_slot(h=0, m=0):
    time_slot = {'hour': h, 'minute': m}
    return time_slot


def set_h_min(time_slot, h, m):
    time_slot['hour'] = h
    time_slot['minute'] = m


def get_h_m(time_slot):
    return time_slot['hour'], time_slot['minute']


def set_min(time_slot, m):
    minutes_in_hour = 60
    time_slot['hour'] = int(m / minutes_in_hour)
    time_slot['minute'] = m % minutes_in_hour


def get_m(time_slot):
    minutes_in_hour = 60
    return time_slot['hour'] * minutes_in_hour + time_slot['minute']


"---------------------------------------------------------------------------------------------"
# main (CLIENT)

"""
The point is that this client can use my module without any information about 
the way in which my module store the time
I could implement create_time_slot storing only minutes and not hours  """

t1 = create_time_slot()
set_h_min(t1, 2, 20)
print(get_h_m(t1))
print(get_m(t1))
set_min(t1, 300)
print(get_m(t1))
print(get_h_m(t1))
