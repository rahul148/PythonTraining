
num=int(input("enter the number:"))
flag=1
def prime(num):
    for i in range(2,num//2+1):
        
        if(num%i==0):
            flag==0
            break
        result=flag
result=prime(flag)
if(flag==1):
    print(num," is s prime number")
else:
    print("the number is not prime")
