words = ["apple", "banana", "cherry", "avocado", "blueberry", "kiwi"]

unique = {word[0].lower() for word in words}

print(unique)   # {'a', 'b', 'c', 'k'}
