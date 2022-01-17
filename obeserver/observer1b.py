# THE OBSERVER

class Subscriber:
    def __init__(self, name):
        self.name=name
    def update(self, message, v):
        print(self.name, '->', message, 'new value: ', v)


# The Observable

class Publisher:
    def __init__(self):
        self.subscribers = set()
        self._a=0

    @property 
    def a(self):
        return self._a
        
    @a.setter
    def a(self, v):
        if v >=0 and v != self.a:
            self._a = v 
            self.dispatch(" The value of <a> has changed!")    
    

    def register(self, an_observer):
        self.subscribers.add(an_observer)

    def unregister(self, an_observer):
        self.subscribers.discard(an_observer)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message, self.a)
        
        

    
    


# driver

publisher = Publisher()  # the observed object
bob = Subscriber('Bob')  # an observer
alice = Subscriber('Alice')  # an observer
john = Subscriber('John')  # an observer

# add the observers to the subscribers' set of the publisher
publisher.register(bob)
publisher.register(alice)
publisher.register(john)

# please note that a subscriber can register itself by calling `publisher.register(self)`

print(publisher.a)
print("\nstep 1\n") 
# subscribers receive a message 
publisher.a = 10
print(publisher.a)

print("\nstep 2\n")
# subscribers DON'T receive a message - because the value does not change
publisher.a = 10
print(publisher.a)

print("\nstep 3\n")
# subscribers DON'T receive a message - because the value does not change
publisher.a = -10
print(publisher.a)

print("\nstep 4\n")
# subscribers receive a message 
publisher.a = 5
print(publisher.a)

publisher.unregister(bob)
publisher.unregister(alice)

print("\nstep 5\n")
# subscribers receive a message 
publisher.a = 50
print(publisher.a)










