list_given = ["apple", "orange", "grapes", "kiwi", "mango"]

result = [x for row in list_given for x in row if x not in 'aeiou']

print(result)