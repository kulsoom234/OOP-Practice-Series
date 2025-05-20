# # # #   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

# # 9. abstract classes and methods
# # assignment:
# # use the ABC module to  create an abstract class shape with an abstarct methor area. inherit a class rectangle
# # that implements area().

# solution

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectangle(8,10)
print("Area of Rectangle:", rect.area())
