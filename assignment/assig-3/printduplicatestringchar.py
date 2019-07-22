#count the repeated character given in string
def countchar(string1):
    list1=[]
    for char in string1:
        if string1.count(char)>=2: 
            if char not in list1:
                list1.append(char)
    for item in list1:
        if item!="":
            print(item,string.count(item))
    else:
        print("->No repeated characters in string......")
string=str(input("enter the string to find reapeating characters\n"))
countchar(string)
