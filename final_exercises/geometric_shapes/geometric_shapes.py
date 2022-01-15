from abc import ABC, abstractmethod


class GeometricShape(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def display_on(self, display):
        pass


class Polygon(GeometricShape):

    def __init__(self, coord = [[1, 1], [2, 1], [2, 2], [1, 2], [0.5, 1.5]]):
        self.coord = coord

    # first dispatch
    def display_on(self, display):
        display._display_polygon(self)


class Ellipse(GeometricShape):

    def __init__(self, x_center=1, y_center=0.5, x_radius=2, y_radius=1.5):
        self.y_radius = y_radius
        self.x_radius = x_radius
        self.y_center = y_center
        self.x_center = x_center

        # first dispatch

    def display_on(self, display):
        display._display_ellipse(self)


# class SomethingElse(GeometricShape)
