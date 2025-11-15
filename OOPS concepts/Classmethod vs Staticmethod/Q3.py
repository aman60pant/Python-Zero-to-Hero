# Create Student class:
# @classmethod count_students(cls) to count objects created
# @staticmethod validate_marks(marks) → return True if 0 ≤ marks ≤ 100.


class Student:
    count = 0

    def __init__(self, name, marks):
        if not Student.validate_marks(marks):
            raise ValueError("marks must be between 0 and 100")
        self.name = name
        self.marks = marks
        Student.count += 1

    @classmethod
    def count_students(cls):
        return cls.count

    @staticmethod
    def validate_marks(marks):
        return 0 <= marks <= 100

s1 = Student("Aman", 69)
s2 = Student("Ravi", 95)
# s3 = Student("Priyanshu", 195) # Raise value error

print(f"{s1.name} valid marks? {Student.validate_marks(s1.marks)}")
print(f"{s2.name} valid marks? {Student.validate_marks(s2.marks)}")
# print(f"{s3.name} valid marks? {Student.validate_marks(s3.marks)}")
print("Total students:", Student.count_students())
