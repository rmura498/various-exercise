"""
Design a class whose instances can store a set of items.
implementing using inheritance and composition.
The items can be supplied one at a time, using the add_item() method
or even in groups, using the add_collection() method.
The object must store the first element, skip the secondo one, store the third and so on.
The object must respond only to methods add_item() and ad_collection()
"""

"""
If i have an object that contains behavior that i wish to reuse i can extend 
the class using inheritance, but sometimes is better to keep the object and 
design a class that contain this object or server and from this inner object 
uses only the behavior that i need

"""

"""
Another situation in which composition could be better:
if you have two classes, for example a list and a class that performs mathematical operations.
You can inherit from both of them, but this make the design more complex, 
so the idea is to implement a new class 
with two attributes, one from the math class and the other from the list class, 
and you can design your interface that 
uses exactly and only the behavior that you want to use    
"""


class AlternateListComp():
    def __init__(self):
        self.list = []
        self._last_index = 0

    def add_item(self, item):
        print("add_item")
        if self._check_index():
            self.list = self.list + [item]

    def add_collection(self, collection):
        print("add_collection")
        for item in collection:
            self.add_item(item)

    def _check_index(self):

        if self._last_index == 0:
            self._last_index = 1
            return True

        else:
            self._last_index = 0
            return False


obj = AlternateListComp()
obj.add_item(24)
obj.add_collection([1, 2, 3, 4, 5, 6])

print(obj.list)

