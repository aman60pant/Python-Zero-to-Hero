# Make two classes A and B(A) where A has method info().
# Override info() in B but still call parent method via super().


class A:
    def info(self):
        print("Info method of base class...")

class B(A):
    def info(self):
        print("Info method of derived class...")
        super().info()

obj = B()
obj.info()
