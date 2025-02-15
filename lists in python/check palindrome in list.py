list1=[]
list1.append(input("Enter something : "))
list1.append(input("Enter something : "))
list1.append(input("Enter something : "))
list1.append(input("Enter something : "))
list2=[]
list2=list1.copy()
print(list1)
list2.reverse()
print(list2)
if(list1==list2) :
    print("List is palindrome.")
else :
    print("Entered list is not pallindrome.")