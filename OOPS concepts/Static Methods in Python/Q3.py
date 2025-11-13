# Create a class Utility having both normal and static methods to demonstrate the difference in usage.

class Utility:
    def non_static(self):
        print("This is a non static method....")

    @staticmethod
    def static_method():
        print("This is a static method....")


u = Utility()
u.non_static()
Utility.static_method()
