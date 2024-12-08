from shape import Shape
import math

class Triangle(Shape):
    def __init__(self, _color, side1, side2, side3):
        #Initilizae a triangle with color and three sides

        Shape.__init__(self, _color)

        #Check to see is these sides can make a triangle
        if (side1 <= 0 or side2 <= 0 or side3 <=0 or
            side1 + side2 <= side3 or
            side1 + side3 <= side2 or
            side2 + side3 <= side1):
            raise ValueError("Invalid triangle: sides cannot form a real triangle")
        
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def get_type(self):
        #tells what type of shape
        return "triangle"
    
    def get_description(self):
        #Creates description of triangle
        return f"{self._color} triangle with sides {self._side1}, {self._side2}, {self._side3}"
    

    def get_perimeter(self):
        #Calculates the total distance around the triangle

        return self._side1 + self._side2 + self._side3
    
    def get_area(self):
        #Calculate the area of the triangle

        #First calculate the semi perimeter
        s = self.get_perimeter() / 2

        # I am using a formula called herons formula
        area = math.sqrt(            
            s *
            (s - self._side1) *
            (s - self._side2) *
            (s - self._side3)
            )

        

        return area
    

    def get_side1(self):
        return self._side1
    

    def get_side2(self):
        return self._side2
    
    def get_side3(self):
        return self._side3
    
