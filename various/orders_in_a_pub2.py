from abc import ABC, abstractmethod


class Customer(ABC):

    def __init__(self):
        self.bill = 0

    @abstractmethod
    def add_drink(self, drink, cost):
        pass

    @staticmethod
    @abstractmethod
    def get_actual_dress():
        pass

    def print_bill(self):
        return self.bill


class CustomerNormalHour(Customer):

    def add_drink(self, drink, cost):
        self.bill += drink * cost

    @staticmethod
    def get_actual_dress():
        return "Normal dress"


class CustomerHappyHour(Customer):

    def add_drink(self, drink, cost):
        discount = 0.5
        self.bill += drink * cost * discount

    @staticmethod
    def get_actual_dress():
        return "Happy Hour dress"


# NORMAL BILLING
customer1 = CustomerNormalHour()
customer1.add_drink(1, 7)
print(customer1.get_actual_dress())
# START HAPPY HOUR (50% discount)
customer1.__class__ = CustomerHappyHour
# You are changing class at runtime!
# It is possible, but are we sure it is a good idea?
customer1.add_drink(2, 5)
print(customer1.get_actual_dress())
# FINAL BILL
customer1.get_actual_dress()
print(customer1.print_bill())
