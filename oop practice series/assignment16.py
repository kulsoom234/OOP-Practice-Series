# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

# 16. Function Decoration:
# assignment:
# write a decorator function log_function_call that prints "function is being called" before a function executes. apply it to a
# function say_hello()

# solution:

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
