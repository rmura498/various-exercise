import copy


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
    def __init__(self, engine, wheels, seats):
        self.engine = engine
        self.wheels = wheels
        self.seats = seats

    @property
    def displacement(self):
        return self.engine.displacement

    @property
    def wheels_pressure(self):
        return [el.pressure for el in self.wheels]

    @property
    def n_seats(self):
        return len(self.seats)


if __name__ == '__main__':
    engine = Engine(2000)
    wheels = [Wheel(7) for i in range(4)]
    seats = [Seat(color=3) for i in range(5)]

    car = Car(engine, wheels, seats)
    print('displacement:', car.displacement)
    print('wheel pressure:', car.wheels_pressure)
    print('n seats:', car.n_seats)
