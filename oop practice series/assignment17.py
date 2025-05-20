# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
# 17. CLASS DECORATORS:
# assignment:
# create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from decorator!" 
# apply it to a class person.

# solution:

def add_greeting(cls):
    def greet(self):
        return "Hello From Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class person:
    def __init__(self , name):
        self.name = name

    def introduce(self):
            return f" My name is{self.name}"
        
person = person("kulsoom")
print(person.introduce())
print(person.greet())

