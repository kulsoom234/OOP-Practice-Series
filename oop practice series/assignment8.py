# # #   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

# 8. the super () function

# assignment:
# create a class person with a constructor that sets the name . inherit a class teacher from it add a subject field, 
# and use super () to call the base class constructor.

# solution:

class person:
   def __init__(self, name):
      self.name = name
      print(f"Person created with the name: {self.name}")

class Teacher(person):
   def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject
    print(f"Teacher teaches: {self.subject}")

t = Teacher("kulsoom" , "GIAIC course")
        