import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

"""
Define a Contact class. Instances have attributes name and email.
When the object is instantiated, name and email are initialized, 
and the email address's formal correctness is checked
Instances have a methods who_i_am() that returns a string
composed by name and email 

"""


class Contact(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.is_valid(value):
            self._email = value
        else:
            self._email = '(missing email)'

    def who_i_am(self):
        return self.name + '' + str(self.email)

    @staticmethod
    def is_valid(email):
        """@staticmethod is a decorator for standalone functions. In this type of function there isn't the instance
        like self. ...."""
        if re.fullmatch(regex, email):
            return True
        else:
            return False


"""
Supplier (sub of contact) has a method order() to place 
purchase orders (the method merely prints a string)

Friend (sub of contact) stores the phone number during its creation

"""


class Supplier(Contact):

    def order(self, order):
        print("Purchase order placed:", order)


class Friend(Contact):

    def __init__(self, name, email, phone=None):
        """Phone attribute has 'none' as default value.
        This is because we need that the interfaces of our parent and child class are
         merely the same. In this way we can, for example, link the name of the class
         and use the interface of these in the same way
          without considering different interfaces"""

        """The liskov substitution principle says that object of a 
        subclass can replace object of the superclass without breaking the application
        Function or methods that use object of a base classes must be able to use objects of
        derived classes without knowing it"""


        super().__init__(name, email)
        self.phone = phone


c = Contact('John Red', 'john@gmail.com')
s = Supplier('Jim Black', 'jim@gmail.com')
f1 = Friend('Sue Whita', 'sue@gmail.com', '123123')
f2 = Friend('Ann Gray', 'ann.gmail.com', '777777')

print(c.who_i_am())
print(s.who_i_am())
s.order('a_thing')
print(f1.who_i_am(), ' ', f1.phone)
print(f2.who_i_am(), ' ', f2.phone)
f2.email = 'correct.email@abc.com'
print(f2.who_i_am(), ' ', f2.phone)
