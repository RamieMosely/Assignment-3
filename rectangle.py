from shape import Shape
import math

class Rectangle(Shape):
    #Rectangle shape with length and width

    def __init__(self, color, length, width):
        #Initialize a rectangle with color, length and width
        Shape.__init__(self, color)

        #Check the dimensions
        if length <= 0 or width <= 0:
            raise ValueError("Length and Width must be positive")
        
        self._length = length
        self._width = width

    def get_type(self):
        #Returns what type of shape
        return "rectangle"
    
    def get_description(self):
        #Returns a description of the rectangle
        return f"{self._color} rectangle with length {self._length} and width {self._width}"
    
    def get_perimeter(self):
        #Calculates the perimeter of the rectangle
        return 2 * (self._length + self._width)
    
    def get_area(self):
        #Calculates the area of the rectangle
        return self._length * self._width
    

    def get_length(self):
        return self._length
    

    def get_width(self):
        return self._width