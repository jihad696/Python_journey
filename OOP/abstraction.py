import math
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        return 0  
    @abstractmethod
    def describe(self):
        return "This is a shape"
    

# sh = Shape() #TypeError
class Square(Shape):
    def describe(self):
        return "This is a Square"
    

# sq = Square() #Typeerror
    


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2)

    def describe(self):
        return f"Circle with radius {self.radius} and area {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 

    def describe(self):
        return f"Rectangle with width {self.width}, height {self.height} and area {self.area()}"


class Triangle(Shape):
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  

    def describe(self):
        return f"Triangle with base {self.base}, height {self.height} and area {self.area()}"  
    


def print_area(shape):
    print(shape.area())


rec = Rectangle(25,12)
print_area(rec)
print(rec.describe())

tr = Triangle(12,10)
circle = Circle(0.35)

obj = [rec , tr , circle]

for i in obj:
    print_area(i) #duck 
    print(i.describe())
    
