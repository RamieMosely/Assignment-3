#Ramie Mosely
# Shape Collection Program
# PROG10004 
#Assignment 3

from shape import Shape
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from square import Square
from pentagon import Pentagon

class Program:
    def __init__(self):
        self._shapes = []

        self._removed_shapes = 0




    def run(self):

        print("Welcome to the Shape Collection Programs!")
        print("Create and manage your own shapes! Woohoo!!")

        #Keeps showing the menu
        while True:
            self.display_menu()
            choice = input("Pick option: ").strip()

            try:
                if choice == '1':
                    self._add_shape()
                elif choice == '2':
                    self._remove_shape()
                elif choice == '3':
                    self._show_shape_info()
                elif choice == '4':
                    self._show_collection_stats()
                elif choice == '5':
                    print("Thank you! GoodBye! <3")
                    break
                else:
                    print("Uh Oh! You entered an invalid command silly! Try again!")
            
            except Exception as e:
                print(f"Error! Something went wrong! {str(e)}")
                print("Please try again!")




    def display_menu(self):
        print(f"\nCollection has {len(self._shapes)} shapes.")
        print("what would you like to do?")
        print("(1) Add a shape")
        print("(2) Remove a shape")
        print("(3) Get information about a shape")
        print("(4) See collection statistics")
        print("(5) Quit program")




    def _add_shape(self):

        print("\nWhat type of shape would you like to add?")
        print("(1) Rectangle")
        print("(2) Triangle")
        print("(4) Square")
        print("(5) Pentagon")

        shape_choice = input("Choose shape type (or just press Enter to go back): ").strip()

        if not shape_choice:
            return
        
        color = input("What color should it be? ").strip().lower

        try:
            if shape_choice == '1':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                new_shape = Rectangle(color, length, width)

            elif shape_choice == '2':
                side1 = float(input("Enter first side length: "))
                side2 = float(input("Enter second side length: "))
                side3 = float(input("Enter third side length: "))
                new_shape = Triangle(color, side1, side2, side3)

            elif shape_choice == '3':
                radius = float(input("Enter radius: "))
                new_shape = Circle(color, radius)

            elif shape_choice == '4':
                side = float(input("Enter side length: "))
                new_shape = Pentagon(color, side)
            
            elif shape_choice == "5":
                side = float(input("Enter side length: "))
                new_shape = Pentagon(color, side)
                
            else:
                print("That is not a valid type of shape!")
                return
            
            self._shapes.append(new_shape)
            print(f"\nGreat! {new_shape.get_description()} has been added to the collection")

        except ValueError as e:
            print(f"Uh oh! {str(e)}")




    def _remove_shape(self):
        if not self._shapes:
            print("\nThere are no shapes to remove!")
            return
            
        print("\nWhich shape would you like to remove!")
        for i, shape in enumerate(self._shapes, 1):
            print(f"({i}) {shape.get_description()}")

        choice = input("Enter the number to remove or press Enter to go back: ").strip()
            
        if not choice:
            return
            
        try:
            index = int(choice) - 1

            if 0 <= index < len(self._shapes):
                    removed_shape = self._shapes.pop(index)
                    self._removed_shapes += 1
                    print(f"\n{removed_shape.get_description()} has been removed.")

            else:
                print("\nThats not a valid shape number!")

        except ValueError:
            print("\nPlease enter a valid number!")




    def _show_shape_info(self):
        #Shows all the details about the shape
        if not self._shapes:
            print("\nThere are no shapes to show!")
            return

        print("\nWhich shapes would you like to know more about?")
        for i, shape in enumerate(self._shapes, 1):
            print(f"({i}) {shape.get_description()}")

        choice = input("Enter a number or press enter to go back! ").strip()

        if not choice:
            return
            
        try:
            index = int(choice) - 1

            if 0 <= index < len(self._shapes):
                shape = self._shapes[index]
                print(f"\n{shape.get_description()}")
                print(f"Perimeter: {shape.get_perimeter():.2f}")
                print(f"Area: {shape.get_area()}")

            else:
                print("\nUh Oh! Thats not a valid shape number!")
            
        except ValueError:
            print("\nPlease eneter a valid number!")



    def _show_collection_stats(self):

        if not self._shapes:
            print("\nThere are no shapes in the collection")
            return
        
        print("\nCollection Statictics:")
        print(f"Total shapes in collection: {len(self._shapes)}")
        print(f"Total shapes ever created: {Shape.s_count}")
        print(f"Shapes removed: {self._removed_shapes}")

        shapes_types = set(shape.get_type() for shape in self._shapes)
        print(f"Types of shapes: {shapes_types}")

        colors = set(shape.color for shape in self._shapes)
        print(f"Colors used: {colors}")

        total_area = sum(shape.get_area() for shape in self.shapes)
        print(f"Total area of all shapes: {total_area:.2f}")

shape_program = Program()
shape_program.run()


