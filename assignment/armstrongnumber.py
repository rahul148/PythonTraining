#write program to find armstrong number
num=int(input("enter the number to check it is armstrong no. or not"))
temp=num
sum=0
n=len(str(temp))
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp=temp//10
 
if(sum==num):
    print("armstrong num")
else:
    print("not armstrong num")
    


for i in range(10):
    num=i
    result=0
    n=len(str(i))
    






