# Create a class Converter with static methods:
# to_celsius(fahrenheit)          # to_fahrenheit(celsius)
# Test without creating any object.

class Converter:
    @staticmethod
    def to_celsius(fahrenheit):
        return (5/9)* (fahrenheit-32)
    
    @staticmethod
    def to_fahrenheit(celsius):
        return (9/5)*celsius+32
    

print(Converter.to_celsius(40))
print(Converter.to_fahrenheit(20))