# Create a class MathOps with static method add(a, b) returning the sum.
# Call it using both class and object.

class MathOps:
    @staticmethod
    def add(a, b):
        return a + b
    

res = MathOps.add(2, 5)

obj = MathOps()
result = obj.add(5, 3)

print(f"with class: {res}.")
print(f"with object: {result}.")