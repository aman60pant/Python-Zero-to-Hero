# Create Temperature class with:
# property celsius
# property fahrenheit that converts automatically.
# Setting fahrenheit should also update celsius.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5)+ 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature(0)
print(t.celsius, t.fahrenheit)
t.fahrenheit = 212
print(t.celsius, t.fahrenheit)