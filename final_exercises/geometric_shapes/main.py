from display import Display1, Display2
from geometric_shapes import Polygon, Ellipse

p1=Polygon()
e1=Ellipse()

d1=Display1()
d2=Display2()

p1.display_on(d1)
p1.display_on(d2)
e1.display_on(d1)
e1.display_on(d2)


"""
From the point of view of the Open-Closed principle, with double dispatch, i can add new classes and new behavior 
following the principle itself. The code is open for extension (because i can easily add new classes) but closed for 
modification because i don't need to change my existing code to add new classes.   
With modularity i have the separation of concerns and with different modules it's easier to understand and implement 
the code. Each module is designed2.
 
 with the capability to run as a standalone script, to explain how to use it 
or testing it. 

"""