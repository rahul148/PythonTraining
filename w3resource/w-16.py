#write progrma to get difference between given number and 17 and return the double of diffenece if the difference is greater then 17
n=int(input("enter the number"))
d=n-17
if(n<17):
    print("the difference is less then 17::",d)
else:
    d1=d+d #or d1=d*2
    print("the difference is greater then 17 then double it::",d1)
#by using function
def difference(n):
    if n<17:
        return 17-n
    else:
        return(n-17)*2
print(difference(22))
print(difference(14))
