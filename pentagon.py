from shape import Shape
import math

class Pentagon(Shape):

    def __init__(self, color, side):

        Shape.__init__(self, color)

        if side <= 0:
            raise ValueError("Pentagon side must be greater than zero!")
        
        self._side = side

    def get_type(self):
        #Tells us the type

        return "pentagon"
    
    def get_description(self):

        return f"{self._color} pentagon with side {self._side}"

    def get_perimeter(self):
        #Gives us perimeter

        return 5 * self._side

    def get_area(self):
        #gives us area

        inner_sqrt = 5 + (2 * math.sqrt(5))
        big_sqrt = math.sqrt(5 * inner_sqrt)

        area = (1/4) * big_sqrt * (self._side * self._side)

        return area
    
    def get_side(self):
        #Gives us the length of a side

        return self._side
    
    def _get_apothem(self):
        #This is a helper method

        angle_in_radians = math.pi / 5
        return self._side / (2 * math.tan(angle_in_radians))

