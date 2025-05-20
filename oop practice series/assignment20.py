# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
# 20. CREATING A CUSTOM Exception
# assignment:

# create a custom exception InvalidAgeError. write a function check_age(age) that raise this exception if age < 18
# handle it with try...except.
    
# solution:

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Age is valid")


try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invali Input. Please enter a valid age.")
    