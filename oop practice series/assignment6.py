# #   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

# assignment:
#  create a class logger that prints a message when an  object is created (constructor)
# and another message when it is destroyed (destructor).

# solution:

class Logger:
    def __init__(self):
        print("Message Before: Logger Object Created.")  # constructor message...!

    def __del__(self):
        print("Message After: Logger Object Destructor.")

log = Logger()
del log


        