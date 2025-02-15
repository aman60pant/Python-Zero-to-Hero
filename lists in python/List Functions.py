## Reverse a list
List1 = [100, 200, 300, 400, 500]
List1.reverse()
print(List1)

## Concatenate 2 lists index wise
List2 = ["m", "na", "i", "Am"]
List3 = ["y", "me", "s", "an"]
List4 = [i + j for i, j in zip(List2, List3)]
print(List4)

## Turns every no in a list to it's square
List5 = [1, 2, 3, 4, 5, 6, 7]
List5 = [ v**2 for v in List5]
print(List5)

## Printing a possible combinations of two lists
List1 = ["Hello", "Take"]
List2 = ["Dear", "Sir"]
List = [x + y for x in List1 for y in List2]

# Another way to do it
#List = []
# for i in range(2):
#     for j in range(2):
#         List.append(List1[i] + " " + List2[j])
print(List)

## Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)