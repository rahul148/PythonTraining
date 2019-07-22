#write program to find its prime number or not.
n=int(input("enter the number"))
count=0
for i in range(2,n//2,1):
    count=count+1
    break#if number is directly divisible by i 
if(count==0 and count!=1):
    print("its prime number\n")
else:
    print("no. is not prime")
