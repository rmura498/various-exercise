class Segment:
    def __init__(self, events):
        self.x = [0, 1]
        self.y = [2, 2]
        self.subscribers = {event: dict() for event in events}

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value[0] == 0 and value[1] == 0:
            self.dispatch('too_small', 'Too small segment')
        elif value[0] > 5 or value[1] > 5:
            self.dispatch('too_big', 'Too big segment ')
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value[0] == 0 and value[1] == 0:
            self.dispatch('too_small', 'Too small segment')
        elif value[0] >= 5 or value[1] >= 5:
            self.dispatch('too_big', 'Too big segment ')
        else:
            self._y = value

    def get_subscribers(self, event):
        return self.subscribers[event]

    def unregister(self, event, an_observer):
        del self.get_subscribers(event)[an_observer]

    def register(self, event, an_observer, callback=None):

        default_method = 'update'
        if callback is None:
            callback = getattr(an_observer, default_method)
        self.get_subscribers(event)[an_observer] = callback

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


class Observer:

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, ' (update method) received the message ', message)


segment = Segment(['too_small', 'too_big'])

oss1 = Observer('oss1')
oss2 = Observer('oss2')
oss3 = Observer('oss3')

print(segment.subscribers)

segment.register('too_small', oss1)
segment.register('too_big', oss2)
segment.register('too_small', oss3)

print(segment.subscribers)

# segment.x = [0, 0]
# segment.y = [5, 5]
