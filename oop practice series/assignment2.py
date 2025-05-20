#   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

#  2. using cls:
#  Assignmets:
#   create a class counter that keeps track of how many objects have been created. use a class variable
# and a class method wity cls to manage and display the counter



#  solution:
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My Total Created Objects Are: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()
obj6 = Counter()
obj7 = Counter()
obj8 = Counter()
obj9 = Counter()
obj10 = Counter()
obj11 = Counter()
obj12 = Counter()

Counter.display_counter()



