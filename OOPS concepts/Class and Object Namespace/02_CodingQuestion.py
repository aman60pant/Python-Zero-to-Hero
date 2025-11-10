# Write a program to show that changing a class variable affects all objects unless overridden by an instance variable.
class Checking:
    check = True

obj = Checking()
print(obj.check)

Checking.check = False

print(obj.check)