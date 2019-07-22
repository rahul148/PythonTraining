def searchl(list,num):
    for i in range(0,len(list)):
        #num=(list1.find())
        if list[i]==num:
            return i
    return -1
list1=[10,20,30,40,50]
no=int(input("Enter number:"))
res=searchl(list1,no)
if res==-1:
    print("no not found.")
else:
    print(res,"found in list.")
