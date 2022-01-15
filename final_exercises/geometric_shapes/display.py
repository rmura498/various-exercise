from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np


class Display(ABC):
    edge_color = None
    face_color = None

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def __init__(self, h, l, bit):
        pass

    @abstractmethod
    def _display_polygon(self, polygon):
        pass

    @abstractmethod
    def _display_ellipse(self, ellipse):
        pass

    @classmethod
    def drawing(cls, xs, ys, fig_size, dpi):

        plt.figure(figsize=fig_size, dpi=dpi, facecolor=cls.face_color,
                   edgecolor=cls.edge_color, )
        plt.title(str(cls.__name__))
        plt.plot(xs, ys)
        plt.show()


class Display1(Display):
    face_color = '#1f77b4'
    edge_color = '#e377c2'

    def __init__(self, h=6.4, l=6.4, bit=100):
        self.fig_size = [h, l]
        self.bit = bit

    """
    In the _display_things parts, each _display function has too many responsibilities
    An idea to improve the code is to define a function for each GeometricShape that compute
    itself xs and ys
    so you can call for example in display polygon 
    xs, ys= polygon.compute_xs_ys
    
    Or better i can store the xs and ys values directly in the __init__ function
    and compute them with the setters.
     
    """

    # second dispatch
    def _display_polygon(self, polygon):
        polygon.coord.append(polygon.coord[0])
        xs, ys = zip(*polygon.coord)

        Display1.drawing(xs, ys, self.fig_size, self.bit)

    def _display_ellipse(self, ellipse):
        t = np.linspace(0, 2 * np.pi, 100)
        xs = ellipse.x_center + ellipse.x_radius * np.cos(t)
        ys = ellipse.y_center + ellipse.y_radius * np.sin(t)

        Display1.drawing(xs, ys, self.fig_size, self.bit)

    # def _display_something_else(self, something).....
    # compute xs, ys
    # drawing

class Display2(Display):
    face_color = '#ff7fb4'
    edge_color = '#aa77c2'

    def __init__(self, h=5, l=5, bit=80):
        self.fig_size = [h, l]
        self.bit = bit
    #second dispatch
    def _display_polygon(self, polygon):
        polygon.coord.append(polygon.coord[0])
        xs, ys = zip(*polygon.coord)

        Display2.drawing(xs, ys, self.fig_size, self.bit)

    def _display_ellipse(self, ellipse):
        t = np.linspace(0, 2 * np.pi, 100)
        xs = ellipse.x_center + ellipse.x_radius * np.cos(t)
        ys = ellipse.y_center + ellipse.y_radius * np.sin(t)

        Display2.drawing(xs, ys, self.fig_size, self.bit)