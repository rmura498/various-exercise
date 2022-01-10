"""
Code that works with Rectangle must work also with the Square class
"""


class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if type(value) == int:
            self._a = value
        else:
            raise TypeError("The value is not a integer")

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if type(value) == int:
            self._b = value
        else:
            raise TypeError("The value is not a integer")


class Square(Rectangle):

    def __init__(self, a, b=0):
        super().__init__(a, a)


print("Rectangle")
r1 = Rectangle(1, 2)
print(r1.a, r1.b)
r1.a = 10
print(r1.a, r1.b)

print("Square")
s1 = Square(2)
print(s1.a, s1.b)
s1.b = 10
print(s1.a, s1.b)
