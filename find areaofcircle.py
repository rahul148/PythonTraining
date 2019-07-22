#find the area of circle
n=float(input("Enter the redius of circle::"))
pi=3.14
Area=pi*n*n
print("Area of the given redius circle::",Area)

#other way by using importing inbuild model
from math import pi
r=float(input("enter the readius of circle::"))
print("the area of circle with given radius"+str(r)+"is:",pi*r**2)
