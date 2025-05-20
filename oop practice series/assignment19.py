# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
# 19. CALLABLE() AND __CALL__ ()
# assignment:

# create a class multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the
# factor test it with  callable()  and by calling the object like a function.
 
# solution:

class Multiplier:
    def __init__(self , factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
    # create an instance of multiplier
double = Multiplier(2)
triple = Multiplier(3)

# test with callable
print(callable(double))
print(callable(triple))

# call the object like a function
print(double(5))
print(triple(5))

# more tests
print(double(10))
print(triple(10))
