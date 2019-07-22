num=int(input("\nenter the number: "))
a=num
if(a<0):
    print("enter the positive values")
else:
    
    def fact(n):
        fact=1
        for i in range(1,n+1):
        
            fact=fact*i   
        return fact
    result=fact(a)
    print(result)
