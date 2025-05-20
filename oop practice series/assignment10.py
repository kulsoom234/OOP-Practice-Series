# # # # #   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
 
# 10. Instance method:
# assignment:
# create a class dog with instance variables name and breed. add an instance method bark()
#  that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says : Woof Woof Woof!")

dog1 = Dog("Buddy", "German Shepherd")
dog1.bark()
