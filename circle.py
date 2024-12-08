from shape import Shape
import math

class Circle(Shape):
    
    def __init__(self, color, radius):
        #Initializes a circle that has color and a radius

        #This calls the parent class
        Shape.__init__(self, color)

        if radius <= 0:
            raise ValueError("The radius must be positive")

        self._radius = radius

    def get_type(self):
        #Returns what type the shape is
        return "circle"
    
    def get_description(self):
        #This returns a description of the circle
        return f"{self._color} circle with radius {self._radius}"
    
    def get_perimeter(self):
        #Returns the circles circumference
        return 2 * math.pi * self._radius
    
    def get_area(self):
        return math.pi * (self._radius ** 2)
    
    @property
    def radius(self):
        return self._radius