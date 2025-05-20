# #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES 
# assignment: COMPPOSITION
# create a class engine and a class car. use composition by passing an engine object to the car
# class during initialization access a method of the engine class via the car class.

# solution:

class Engine:
    def start(self):
        print("Engine has started...")

class Car:
    def __init__(self):
        self.engine = Engine()   # THIS LINE IS CALLED COMPOSITION.

    def start_car(self):
        self.engine.start()
    
if __name__ == "__main__":
    my_car = Car()
    my_car.start_car()
    
    
