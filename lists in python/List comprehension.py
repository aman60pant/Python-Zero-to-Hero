List = ["Aman", "Vinay", "Ajay", "Anamika", "Priyanshu", "Anmol"]
print(f"List 1 is {List}")
List2 = []

# The below commented lines are the alternate method for performing sorting  
# for name in List:
#     if "A" in name:
#         List2.append(name)
# print(List2)
List2 = [name for name in List if "A" in name]
print(f"List 2 with names starting with 'A' is {List2}")