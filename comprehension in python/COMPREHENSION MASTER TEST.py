# Q1: Basic Transformation (List Comprehension)
# Create a list of squares of all numbers between 1 and 15, but only include those whose square is greater than 50 and less than 200.
list_1 = [num*num for num in range(1, 16) if num*num > 50 and num*num <200]
print(list_1)

# Q2: Conditional Logic (List Comprehension)
# For numbers from 1 to 10, create a list containing "Even" if number is even, and "Odd" otherwise.
List_2 = ["Even" if x%2==0 else "Odd" for x in range(1, 11)]
print(List_2)

# Q3: Flatten Nested List
# Use nested list comprehension to flatten it → [1,2,3,4,5,6,7,8,9].
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [x for row in matrix for x in row]
print(result)

