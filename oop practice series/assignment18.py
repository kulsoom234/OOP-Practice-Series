# # #  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES
# 18. property DECORATORS: @PROPERTY, @SETTER AND @DELETER.
# Assignment:
# create a class product with a private atribute _price. use property to get the price, @price.setter to upload it,
# and @ price.deleter to delete it.

# solution:

class Product:
    def __init__(self , price):
        self._price = price

    @property
    def price(self):
        print("Greeting price")
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0 :
            raise ValueError("price cannot be nagative")
        print("Setting price to ", value)
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price

    
product = Product(100)
print("Initial price:")
print(product.price)

print("\nUpdating price:")
product.price = 150
print(product.price)

print("\nDeleting price")
del product.price

try:
    print(product.price)
except AttributeError:
    print("Price attribute has been deleted")

print("\nTrying to get negative price:")

try:
    product._price = -50
    product.price = -50
except ValueError as e:
    print(e)

    




