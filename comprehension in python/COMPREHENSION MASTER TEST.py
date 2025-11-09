# Q1: Basic Transformation (List Comprehension)
# Create a list of squares of all numbers between 1 and 15, but only include those whose square is greater than 50 and less than 200.
list_1 = [num*num for num in range(1, 16) if num*num > 50 and num*num <200]
print(list_1)