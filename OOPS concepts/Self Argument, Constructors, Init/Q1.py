# Create a class Circle with attribute radius.
# Add a method area() that calculates and returns the area using self.radius.
# Create two circle objects with different radii and print their areas.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

obj1 = Circle(5)
print(obj1.area())

obj2 = Circle(10)
print(obj2.area())