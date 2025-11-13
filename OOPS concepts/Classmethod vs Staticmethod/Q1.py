# Create class Employee with class variable company = "Google".
# Add:
# 👉@classmethod change_company(cls, new_name)
# 👉@staticmethod is_office_day(day) → returns True if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Use both via class and object.


class Employee:
    company = "Google"
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @staticmethod
    def is_office_day(day):
        if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            return True
        return False


print(f"before changing company name: {Employee.company}")
Employee.change_company("Microsoft")
print(f"after changing company name without object: {Employee.company}")

print(Employee.is_office_day("Monday"))

obj = Employee()
print(f"before changing company name: {Employee.company}")
obj.change_company("Amazon")
print(f"after changing company name with object: {Employee.company}")