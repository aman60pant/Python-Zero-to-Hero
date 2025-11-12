# Create a class Employee with a class variable company = "Google". Then:
# Create object emp1 and print emp1.company.
# Assign emp1.company = "Microsoft".
# Print both emp1.company and Employee.company.

class Employee:
    company = "Google"

emp1 = Employee()
print(emp1.company)

emp1.company = "Microsoft"

print(emp1.company)
print(Employee.company)