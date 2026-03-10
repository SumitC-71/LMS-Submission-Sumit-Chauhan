'''
Task 5: Abstraction
    1. Create an abstract class Shape with an abstract method calculate_area().
    2. Create subclasses Rectangle and Circle that inherit from Shape.
        ○ Forthe Rectangle class, use attributes length and width.
        ○ Forthe Circle class, use attribute radius.
    3. Implement the calculate_area method in both subclasses.
    4. Write a program to:
        ○ Create objects of Rectangle and Circle.
        ○ Call the calculate_area method for each object and display the result.

'''

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def calculate_area(self):
        return (22/7) * self.radius * self.radius


rectangle = Rectangle(2,3)
circle = Circle(2)

print("Rectangle Area:", rectangle.calculate_area())
print("Circle Area:", circle.calculate_area())