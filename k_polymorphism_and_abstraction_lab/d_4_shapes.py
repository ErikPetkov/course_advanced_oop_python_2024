from abc import ABC , abstractstaticmethod
from math import pi

class Shape(ABC):
    @abstractstaticmethod
    def calculate_area():
        pass

    @abstractstaticmethod
    def calculate_perimeter():
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return self.radius*self.radius*pi

    def calculate_perimeter(self):
        return  self.radius*2*pi

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height*self.width

    def calculate_perimeter(self):
        return (self.height+self.width)*2


circle = Circle(5)

print(circle.calculate_area())

print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)

print(rectangle.calculate_area())

print(rectangle.calculate_perimeter())