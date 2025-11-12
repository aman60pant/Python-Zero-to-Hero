# Create a class School with a class variable principal = "Mr. Raj".
# Then set an instance variable principal = "Mr. Arjun" for one object.
# Print both to show how attribute shadowing works.

class School:
    principal = "Mr. Raj"


obj = School()
obj.principal = "Mr. Arjun"

print(obj.principal)
print(School.principal)