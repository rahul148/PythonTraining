n=int(input("enter the num"))
flag=1
for i in range(2,n//2+1):
    if(n%i==0):
        flag=0
        break#its used for,if number is directly divisible by and reduce the cpu cylcl
if(flag==1):
    print("is prime")
else:
    print("not prime")
