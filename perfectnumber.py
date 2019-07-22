#practices of perfect number
n=int(input("enter the number to find weather its perfect or not:"))
sum=0
rem=0
for i in range(1,n-1,1):
    rem=n%i
    if(rem==0):
        sum=sum+i
if(sum==n):
    print(n,"is the perfect number.")
else:
    print(n,"is not perfect number")
