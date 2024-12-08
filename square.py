from shape import Shape
import math

class Square(Shape):

    #Creating a new square
    def __init__(self, color, side):

        Shape.__init__(self, color)

        #Check to see if the sides are valid
        if side <= 0:
            raise ValueError("Squares side must be greater than zero")
        

        self._side = side

    def get_type(self):
        #Gives us type of square
        return "square"
    
    def get_description(self):
        #Gives us description of square

        return f"{self._color} square with {self._side}"
    
    def get_perimeter(self):
        #Calculates the distance around the square
        return 4 * self._side
    
    def get_area(self):
        #Calculates the area of the square

        return self._side * self._side
    
    def get_side(self):
        return self._side

