# Create three classes A, B(A), and C(B) — each with method show().
# Create an object of C and call show().
# Print C.mro() to see the resolution order.

class A:
    def show(self):
        print("Method of class A...")

class B(A):
    def show(self):
        print("Method of class B...")

class C(B):
    def show(self):
        print("Method of class C...")

obj = C()
obj.show()

print(C.mro())