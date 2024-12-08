class Shape:
    #This is the base class that represents every 2D shape
    #It provides the common methods and attribute for each shape

    #Static class variable that tracks total shapes created
    s_count = 0

    def __init__(self, color):
        #Initialize shape with a colour
        self._color = color
        Shape.s_count += 1

    def get_type(self):
        #Returns what type the shape is as a string
        return "Generic Shape"
    
    def get_description(self):
        #Returns a desciption as a string about the shape
        return f"{self._color} {self.get_ype()}"
    
    def get_perimeter(self):
        #Calculates the perimeter of shape
        raise NotImplementedError("This subclass needs to implement a method!")

    def get_area(self):
        #Calculates the area of the shape.
        raise NotImplementedError("This subclass needs to implement a method!")


    def get_color(self):
        #color accessor method
        return self._color