#enter the right angle
n=int(input("enter the number row do you want"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()
#other way to it
n=int(input("enter the rows"))
for i in range(1,n+1):
    print("*"*i)#==>"*i" its will multiple the values and show in that row

    
