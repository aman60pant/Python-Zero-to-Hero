list_1 = ["apple", "banana", "cherry", "kiwi", "mango"]

req_list = [item for item in list_1 if len(item) > 5]

print(f"Items with length greater than 5 are {req_list}")