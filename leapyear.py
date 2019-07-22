
#check weather it is leap year or not
num=int(input("enter the year"))
if num%4==0 and num%100!=0 or num%400==0:
    print(num,"this is leap year\n")
else:
    print(num,"this not leap year")
