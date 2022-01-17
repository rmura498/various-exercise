from abc import ABC, abstractmethod


class Publisher:

    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def unregister(self, an_observer, event):
        del self.get_subscribers(event)[an_observer]

    def register(self, an_observer, event, callback=None):
        default_method = 'update'
        if callback is None:
            callback = getattr(an_observer, default_method)
        self.get_subscribers(event)[an_observer] = callback

    def dispatch(self, event, message):
        for subscribers, callback in self.get_subscribers(event).items():
            callback(message)


class Subscriber(ABC):

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def subscriber_method(self, message):
        pass


class SubscriberStateOne(Subscriber):

    def subscriber_method(self, message):

        print(self.name, 'received message:', message)
        print("I am doing some actions")


class SubscriberChangeState(Subscriber):

    def subscriber_method(self, message):
        print(self.name, 'received message:', message)
        print("I am doing other actions")
