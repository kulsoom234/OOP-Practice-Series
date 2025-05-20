#  #  PROJECT : 6 BUILD_COMPOSE_AND_DECORATE_A_COMPLETE_TRADITIONAL_OOP_PRACTICE_SERIES

# assignment:

# create a class temperatureconverter wit a static method celsius_to_fahrenheit 
# that returns a fahrenheit value.

# solution:

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5 +32)
    
celsius = 30
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius}◙C is equal to {fahrenheit}◙F")


