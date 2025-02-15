# Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)

# Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

# Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

# Remove all occurrences of a specific item from a list
list1 = [5, 20, 15, 20, 25, 50, 20]
# list comprehension
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]
res = remove_value(list1, 20)
print(res)
list1 = [5, 20, 15, 20, 25, 50, 20]
# using while loop (slow process)
while 20 in list1:
    list1.remove(20)
print(list1)