#write progrmas to find the factorial of number
n=int(input("enter the number "))
fact=1
for i in range(1,n):
    fact=fact*(i+1);
print("the factorial of number is:",fact)
