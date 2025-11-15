# Create Person class with private variable _age.
# Use:
# @property → getter for age
# @age.setter → validates age must be > 0

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be greater than 0.")
        

p = Person(25)
print(p.age)
p.age = 30
print(p.age)