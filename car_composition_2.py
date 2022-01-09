"""
Write a class using composition.
the creation interface must be the same as that
defined in the case of inheritance.

"""


class Engine():
    def __init__(self, displacement=1000):
        self.displacement = displacement


class Wheel():
    def __init__(self, pressure=10):
        self.pressure = pressure


class Seat():
    def __init__(self, color=1):  # 1, 2, 3
        self.color = color


class Car():
    def __init__(self, displacement, pressure, seats_color, n_seats=5, n_wheels=4):
        self.engine = Engine(displacement)
        self.wheels = [Wheel(pressure) for i in range(n_wheels)]
        self.seats = [Seat(seats_color) for i in range(n_seats)]

    @property
    def displacement(self):
        return self.engine.displacement

    @property
    def wheels_pressure(self):
        return [el.pressure for el in self.wheels]

    @property
    def n_seats(self):
        return len(self.seats)


# CLIENT

car1 = Car(2000, 7, 1)
car2 = Car(2000, 7, 1)
print('displacement:', car1.displacement)
print('wheel pressure:', car1.wheels_pressure)
print('n seats:', car1.n_seats)
print('Seat 1 color:', car1.seats[0].color)