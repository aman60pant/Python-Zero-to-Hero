# Create a class Laptop with a class variable brand = "Dell". Create two objects and print their brand. Then, change the brand for one object and observe the output.
class Laptop:
    brand = "Dell"

obj_1 = Laptop()
print(obj_1.brand)
obj_1.brand = "HP"

obj_2 = Laptop()
print(obj_2.brand)

Laptop.brand = "Acer"
print(obj_2.brand)