print("using print function")
print("Hello this is my first program")




print("Adding two values & displaying the output")
a=5
b=10.5
c=a+b
print(a)
print(b)
print("Sum is ", c)




print("Printing strings")
print("hey whats up")
print('hey whats up')
print('''hey
        whats
            up
      ''')



print("Applying functions in a string")
string2="hey whats up"
print("string is : ",string2)

print("Printing characters of a specific range")
print(string2[1:6])

print("Printing the left string from specific character ") 
print(string2[1::])

print("Printing a reversed string ")
print(string2[::-1])

print("Reversing string")
string2="".join(reversed(string2))
print(string2)

print("Changing character of a string")
string1="Helow User! How are you?"
list1=list(string1)
list1[10]='s'
new_string = ''.join(list1)
print(new_string)

print("deleting a character of a string ")
string2=new_string[0:2]+new_string[3::]
print(string2)

print("deleting a string")
print(new_string)
del new_string

print("Escape sequencing in python")
print("Initial string with the use of Triple Quotes:")
string1='''I'm a "Geek"'''
print(string1)

print("Escaping single quote")
string1='I\'m a "Geek"'
print(string1)

print("Escaping double quote")
string1="I'm a \"Geek\""
print(string1)

print("Escaping backslashes")
string1="C:\\USERS\\Public\\Pictures"
print(string1)

# Printing hello in octal 
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ") 
print(String1) 
  
# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1)






# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1)


# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 
  
# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 
  
# Keyword Formatting 
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life') 
print("\nPrint String in order of Keywords: ") 
print(String1)

print("\x42")
