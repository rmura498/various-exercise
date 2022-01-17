class Publisher:

    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def unregister(self, an_observer, event):
        del self.get_subscribers(event)[an_observer]

    def register(self, an_observer, event, callback=None):
        default = 'update'
        if callback is None:
            callback = getattr(an_observer, default)
        self.get_subscribers(event)[an_observer] = callback

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


class Observer:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(self.name, 'received message:', message)
