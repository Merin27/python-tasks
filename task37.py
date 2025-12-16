from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    
    @abstractmethod
    def calculatePerimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculateArea(self):
        return 3.14 * self.radius ** 2
    def calculatePerimeter(self):
        return 2 * 3.14 * self.radius
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculateArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2 
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3))**0.5
    def calculatePerimeter(self):
        return self.side1 + self.side2 + self.side3
circle = Circle(3)
triangle = Triangle(3, 4, 5)
print(f"Circle - Area: {circle.calculateArea():.2f} , Perimeter: {circle.calculatePerimeter():.2f}")
print(f"Triangle - Area: {triangle.calculateArea():.2f} ,  Perimeter: {triangle.calculatePerimeter():.2f}")
