# Create a base class Person (name, age) and derived class Student (roll_number, course).
# Override a method to print all details using both base and child attributes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll number: {self.roll_number}")
        print(f"Course: {self.course}")

obj = Student("Aman", 22, 10, "BCA")
obj.details()

obj.name = "Priyanshu"
obj.age = 21
obj.roll_number = 2
obj.course = "Bsc"

obj.details()