# Create a class Rectangle with attributes length and width.
# Add a method perimeter() that uses self to calculate perimeter.
# Create multiple objects and show that self points to different instances.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)


obj1 = Rectangle(100, 20)
print(obj1.perimeter())

obj2 = Rectangle(50, 20)
print(obj2.perimeter())

obj3 = Rectangle(100, 30)
print(obj3.perimeter())