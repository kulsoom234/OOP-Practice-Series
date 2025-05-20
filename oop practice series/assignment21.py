# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
# 21. MaKE A CUSTOM CLASS ITERABLE
# Assignment:

# create a class countdown that takes a start number.implement __iter__() and __next__() to make the object iterable 
# in a four-loop,  counting down to 0.

# solution:

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -=1
        return value
    
countdown = Countdown(4)

for num in countdown:
    print(num)

    