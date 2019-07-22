#silcinf with string.................
str1="hello world"
print(str1[2:5])##o/p:"llo"

str1="rahull"
print(str1[0])#it will dsiplay the character which persent at index 0 o/p:"r"


#for with else.............
i=[1,2,3]#if "i" list is empty then it will directly goto the else loop. 
for a in i:
    print("it is in for loop")
else:
    print("it is in else part")


#<<<1>>#The for ... else statement is used to implement search loops.


##In particular, it handles the case where a search loop fails to find anything.

for z in range(10):
    if z == 5:
        # We found what we are looking for
        print("we found 5")
        break # The else statement will not execute because of the break
else:

    # We failed to find what we were looking for
    print("we failed to find 5")
    z = None

print('z = ', z)


#<<2>>>append() and extend() in Python.............................
"""
#Append::
    Adds its argument as a single element to the end of a list.
The length of the list increases by one.
append() takes exactly one argument
"""

mylist=[1,2,3,4]
mylist.append(20)
print(mylist)
"""mylist.append(20,20)
TypeError: append() takes exactly one argument"""

###....import Note...#############....................
"""NOTE: A list is an object. If you append another list onto a list,
the first list will be a single object at the end of the list.

"""
my_list = ['geeks', 'for', 'geeks'] 
another_list = [6, 0, 4, 1] 
my_list.append(another_list) 
print(my_list)

##---extend():

"""     Iterates over its argument and adding each element to the list and extending the list.
        The length of the list increases by number of elements in it’s argument
"""
mylist=[1,2,3,'rahul']
print(mylist)
newlist=[0,4,5]
mylist.extend(newlist)
print("after extend::",mylist)

###importend Note about extends::###....................
"""
    NOTE:  A string is an iterable, so if you extend a list with a string,
            you’ll append each character as you iterate over the string.
"""

mylist=["rahul",22,33,44]
s='rahul'
mylist.extend(s)
print("list after the strin extends::",mylist)

    #o/p:
        #->>list after the strin extends::
        #['rahul', 22, 33, 44, 'r', 'a', 'h', 'u', 'l']

s=['rahul']
mylist.extend(s)
print("list after the strin extends::",mylist)
    #o/p:
        #"""list after the strin extends::
        #['rahul', 22, 33, 44, 'rahul']"""


#what is output of the following programs::

#a=2,c=3,b=2 #...error-1 ===>..its show the error can't assign the literals
a=2
c=3
b=2
if a==b and c!=a or c==b:
    print("IN the first if statements are excuted......")
###.... c=2 if c==b and b==a:....error-2 ===> invalid syntax...........

c=2    
if c==b and b==a:
    print("Its in second if statement is excuted")
