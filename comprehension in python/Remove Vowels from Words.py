list_given = ["apple", "orange", "grapes", "kiwi", "mango"]

result = [''.join(ch for ch in word if ch.lower() not in 'aeiou') for word in list_given]

print(result)