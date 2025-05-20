# #   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

#  7. access modifier: public, private, and protected
# asignment:
#  create a class employee with :
# a public variables name:
# a protected variables name:
# a protected variable __salary,and
# a private variable __ssn:
# try acessign all three variables from an object of the alass and document what happens:

# IMPORTANT POINTS:

# public (name, department): aam tor pr har jagag accessible.
# protected (_salary): sub class access krskta hai,lekin directly bhar se krna recommended h.
# private(_ssn): sirf class k andr ya getter method se access ho skta hai.

# getter: get_ssn() private data ko safely read karta hai.
# setter: get_salary() protected variables  ko validate kr k set krta h.

# solution:
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name              # public
        self._salary = salary         # protected
        self.__ssn = ssn              # private

    # Getter for private variable __ssn
    def get_ssn(self):
        return self.__ssn

    # Setter for protected variable _salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be a positive number")

    def display(self):
        print(f"Name: {self.name}")         # public
        print(f"Salary: {self._salary}")    # protected
        print(f"SSN: {self.__ssn}")         # private


class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter: {self.get_ssn()}")


# Testing the classes
m = Manager("Ali", 12000, "444-852-2025", "Information Technology")
m.show_manager_info()

# Update salary
m.set_salary(32000)
print("Updated Salary:", m._salary)  # Accessing protected variable (not recommended outside class)

# # Accessing private variable directly (will fail)
# try:
#     print(m.__ssn)
# except AttributeError as e:
#     print("Error accessing private variable directly:", e)

# # Correct way using name mangling (not recommended, just to show it's possible)
# print("Accessing SSN via name mangling (not recommended):", m._Employee__ssn)

