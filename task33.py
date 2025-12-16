# Shape-calculate area

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.radius = int(input("Enter the Radius:"))

    def calculateArea(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.length = int(input("Enter the length:"))
        self.breadth = int(input("Enter the breadth:"))
    
    def calculateArea(self):
        return self.length * self.breadth

circle = Circle('')
print(f"Area of the Circle: {circle.calculateArea()}")

rectangle = Rectangle('','')
print(f"Area of the Rectangle: {rectangle.calculateArea()}")
