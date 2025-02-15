n=int(input("Enter the no of items you want to store in the list : "))

items=[]
for i in range (n):
    items.append(input("Enter the item you want to store :"))

for i in range (n):
    print(f"Item at index {i} is : {items[i]}")

chn= int(input("Enter the index of the item you want to change : "))
items[chn]= (input("Enter the new item : "))
print(items)

chn= int(input("Enter the index of the item you want to Delete : "))
del(items[chn])
print(items)