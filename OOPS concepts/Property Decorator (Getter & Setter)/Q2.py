# Create Rectangle with _length and _width.
# Use property decorators for both.
# Reject negative values and calculate area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Length must be greater than 0.")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be greater than 0.")
        self._width = value

    @property
    def area(self):
        return self._length * self._width
    
obj = Rectangle(5, 10)
print(f"Length: {obj.length}, Width: {obj.width}, area = {obj.area}")