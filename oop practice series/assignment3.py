#   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

# 3. Public Variables nd Methods
#  assignments
#   create a class car with a publiuc variable brand and a public method start(). instantiate the class and access both 
# from outside the class.

# solution:
class Car:
    def __init__(self , brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting..........!")

my_car = Car("Kia Sportage")
print(my_car.brand)
my_car.start()