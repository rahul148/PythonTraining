#n=int(input("enter the number\n"))
count=0
count1=0

for n in range(1,1000,1):
    flag=1
    for i in range(2,n//2+1):
        if(n%i==0):
            flag=0
            break
    if(flag==1):
        count=count+1
        #print("is prime")
    else:
        count1=count1+1
        #print("not prime")
print(count," total is prime number")
print(" total no prime number is:",count1)
