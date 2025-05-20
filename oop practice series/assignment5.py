#   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

#  5. static variables and static methods
#  assignment:
#  create a cl;ass mathutils with a static method add(a,b) that returns the sum. no class or instance varibles 
# should be used.

# solution:

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
result = MathUtils.add(13,44)
print("Sum Of My Desired Numbers Are: ", result)
