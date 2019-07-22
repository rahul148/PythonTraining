#write a progema to find the perfect number
n=0
count=0
count1=0
for n in range(1,500,1):
    sum=0
    rem=0
    for i in range(1,n-1,1):
        rem=n%i
        if(rem==0):
        
            sum=sum+i
    if(sum==n):
        count=count+1
    else:
        count1=count1+1
        
print(count,"total count number")
print(count1,"total not perfect num")
