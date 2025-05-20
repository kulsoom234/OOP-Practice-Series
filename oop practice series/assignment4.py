#   #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

#  class variables and class methods:
# assignments:
#  create a class bank with a class variable bank_name. add a class method change_bank_name(cls, name)
# that allows changing the bank name. show that it affects all instance.

#  solution:


class Bank:
    bank_name = "Islamic Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} , Bank: {self.bank_name}")

account1 = Bank("kulsoom")
account2 = Bank("farrukh")

account1.display()
account2.display()

Bank.change_bank_name("Habib Bank Limited")

account1.display()
account2.display()
