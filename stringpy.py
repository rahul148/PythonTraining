s=str("rahul shinde")
print(s)
#using "*" to print the string multiple time
print(s *2)
#print the character at the given index
print(s[1])
#its only print the character between the given
print(s[0:5])
#using minus we can print the values from (back side index)reverse side of stirng
print(s[-3:-1])
#len function calculate the total length of string including space
print(len(s))
#type fuction show the types of varible class
print(type(s))
#strip is used to remove the white space
print(s.strip())
#its show the starting index of string and find if not found show the values in negative integer index
print(s.find("rahul"))
#count the number occurce in string how many times uisng count.
print(s.count("h"))
#replace the string
print(s.replace("rahul","rohan"))
#uppcase and lower case,title
print(s.upper())
print(s.upper(),s.lower())
print(s.title())
#for reverse string 
"""User must enter a string.
2. By giving the increment value as -1, string slicing is used to reverse the list.
3. The reversed string is printed."""
st=str(input("enter the string"))
print("revers string is :")
print(st[::-1])


