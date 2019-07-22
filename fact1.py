#to find the number is primer or not
num=int(input("enter the number \n"))
count=0
for num in range(1,int(num/2),1):
    if(num%2==0):
        count=count+1
        break
if(count==0 and count!=1):
    print("the number is prime")
else:
 print("the nuber not prime")
