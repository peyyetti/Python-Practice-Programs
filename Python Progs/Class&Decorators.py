
"""
import math as mt
class Circle:
  
  def __init__(self, r):
    self.radius = int(r)
    print(f"Hello! Radius is {self.radius} ")
  
  def perimeter(self):
    self.perimeter = self.radius * 2 * mt.pi
    print(f"Hello! Perimeter is {self.perimeter} ")
  
  def area(self):
    self.area = (self.radius ** 2) * mt.pi
    print(f"Hello! Area is {self.area} ")
    
Circle1 = Circle(1_700)   # pay attention here on the argument
Circle1.perimeter()
# Circle1.area()

"""

# decorators in python
# basically used to modify a function ouput by passing it to other function

def display():
    print("Hello guys! {} function here! ".format(display.__name__))

var = display
var()