#gcd by using the recursive methods
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)#recursive call to function itself 
num1=int(input("enter the first number:  "))
num2=int(input("enter the second number: "))
print(gcd(num1,num2))


#help--https://www.youtube.com/watch?v=cahuG1cEQdY
