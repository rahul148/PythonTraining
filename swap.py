num1=int(input("enter the number\n"))
num2=int(input("enter the second number"))
if(num1==num2):
    print(num1,num2,"same number")
else:
   """ num3=num1
    num1=num2
    num2=num3
    print("after swaping number",num1,num2)"""
   #or-wihtout using third variable
  """ num1=num1+num2
   num2=num1-num2
   num1=num1-num2
   print(num1,num2,"after swap");"""
   #or
   num1,num2=num2,num1
   print(num1,num2,"after swap");
