  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES


#  1. Using_self
 # ASSIGNMENT:
       # Create a class with atributes name and marks. use the self keyword to initialize theese values via 
#  constructor. add a method display() that prints student details

#  solution
class student:
    def __init__(self , name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = student("kulsoom", 97)
student1.display()


