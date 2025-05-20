# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
# 15. METHOD RESOLUTION ORDER (MRO) AND DIAMOND INHERITANCE:

# assignment:
#  create four classes:
# . A with a method show().
# . B and C that inherit from A and override show().
# . D than inherit from both B and C.
# Create an object of D and call show() to observe MRO.

# SOLUTION:

class A:
    def show(self):
        print("show method in class A")

class B(A):
    def show(self):
        print("show method in class B")

class C(A):
    def show(self):
        print("show method in class C")

class D(C , A):
    pass

d = D()
d.show()

print(D.mro())
