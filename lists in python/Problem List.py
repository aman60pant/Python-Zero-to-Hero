List = ["Anil", "Anmol", "Aditya", "Avi", "Alka"]
print(f"The list is {List}")

print("Insert 'Anuj' before 'Aditya'")
List.insert(2, "Anuj")
print(List)

print("Append 'Zulu'")
List.append("Zulu")
print(List)

print("Remove 'Avi")
List.remove("Avi")
print(List)

print("Change 'Anil' to 'AnilKumar'")
ind = List.index("Anil")
List[ind] = "AnilKumar"
print(List)

print("Sort the list in ascending order")
List.sort()
print(List)

print("Sort the list in descending order")
List.sort(reverse=True)
print(List)