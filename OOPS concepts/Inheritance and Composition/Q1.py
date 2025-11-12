# Create a base class Animal with method sound().
# Then make subclasses Dog and Cat that override sound().
# Create objects and call sound() on each.

class Animal:
    def sound(self):
        print("Base class Animal")

class Dog(Animal):
    def sound(self):
        print("Dog barks...")

class Cat(Animal):
    def sound(self):
        print("Car Meow")


dog = Dog()
cat = Cat()
animal = Animal()

dog.sound()
cat.sound()
animal.sound()