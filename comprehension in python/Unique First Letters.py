words = ["apple", "banana", "cherry", "avocado", "blueberry", "kiwi"]

unique = {x for row in words for x in row[0]}

print(unique)