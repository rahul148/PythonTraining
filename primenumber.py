#prime number
n=int(input("enter the number"))
count=0
for n in range(1,int(n/2),1):
    if(n%2==0):
        count=count+1
        break
if(count==0 and count!=1):
    print("the prime number")
else:
    print("the number is not prime")
