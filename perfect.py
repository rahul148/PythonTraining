n=int(input("enter the number\n"))
sum=0
for i in range(1,n-1):
    rem=n%i
    if(rem==0):
        sum=sum+i
if(sum==n):
    print("the number is perfect")
else:
    print("not prime")
