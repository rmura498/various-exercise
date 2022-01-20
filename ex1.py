# COMPLETE THE CODE...



from abc import ABC, abstractmethod

class GeometricShape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw_display1(self, display):
        pass

    @abstractmethod
    def draw_display2(self, display):
        pass


class Rectangle(GeometricShape):

    # second dispatch
    def draw_display1(self, display):
        print("draw the rectangle", self.name,
              'into the display of type 1 :', display.name)

    def draw_display2(self, display):
        print("draw the rectangle", self.name,
              'into the display of type 2 :', display.name)


class Circle(GeometricShape):

    # second dispatch
    def draw_display1(self, display):
        print("draw the circle", self.name,
              'into the display of type 1 :', display.name)

    def draw_display2(self, display):
        print("draw the circle", self.name,
              'into the display of type 2 :', display.name)


from abc import ABC, abstractmethod


class Display(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw(self, geometric_shape):
        pass


class Display1(Display):

    def draw(self, geometric_shape):
        geometric_shape.draw_display1(self)  # first dispatch


class Display2(Display):

    def draw(self, geometric_shape):
        geometric_shape.draw_display2(self)  # first dispatch

if __name__ == '__main__':
    print("\n\n")

    r = Rectangle('**blue rectangle**')
    c = Circle('**big red circle**')
    d1 = Display1('800x600x8')
    d2_a = Display2('1600x1600x16 - A')
    d2_b = Display2('1600x1600x16 - B')

    d1.draw(r)
    d1.draw(c)
    d2_a.draw(r)
    d2_a.draw(c)
    d2_b.draw(r)
    d2_b.draw(c)

    print("\n\n")

    """ OUTPUT:

draw the rectangle  **blue rectangle**  into the display of type 1 : 800x600x8
draw the circle  **big red circle**  into the display of type 1 : 800x600x8
draw the rectangle  **blue rectangle**  into the display of type 2 : 1600x1600x16 - A
draw the circle  **big red circle**  into the display of type 2 : 1600x1600x16 - A
draw the rectangle  **blue rectangle**  into the display of type 2 : 1600x1600x16 - B
draw the circle  **big red circle**  into the display of type 2 : 1600x1600x16 - B

    """
