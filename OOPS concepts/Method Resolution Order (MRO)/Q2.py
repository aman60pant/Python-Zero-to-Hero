#     A
#    / \
#   B   C
#    \ /
#     D

# All have say_hello() method.
# Create object of D and call say_hello() — check output order using D.mro().

class A:
    def say_hello(self):
        print("Method of class A....")

class B(A):
    def say_hello(self):
        print("Method of class B....")

class C(A):
    def say_hello(self):
        print("Method of class C....")

class D(B, C):
    def say_hello(self):
        print("Method of class D....")

obj = D()
obj.say_hello()

print(D.mro())