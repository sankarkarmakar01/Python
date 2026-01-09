from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Square area")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area")

square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()