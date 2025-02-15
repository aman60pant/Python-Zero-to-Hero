#function to perform addition of two numbers
def add(n1, n2):
    return n1 + n2

#function to perform multiplication of two numbers
def multiply(n1, n2):
    return n1 * n2

number1 = 13.98; number2 = 87.65
addition = round(add(number1, number2),4)
print(f"addition of {number1} and {number2} is {addition}")

product = round(multiply(number1, number2),4)
print(f"Product of {number1} and {number2} is {product}")