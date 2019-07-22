#factorial program
n=int(input("enter the non negative number\n"))
fact=1
for i in range(1,n):
    fact=fact*(i+1)
print("the factorial of given number is:",fact)
