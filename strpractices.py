str1="hello world"
print(str1[2:5])##o/p:"llo"

str1="rahull"
print(str1[0])#it will dsiplay the character which persent at index 0 o/p:"r"



i=[1,2,3]#if "i" list is empty then it will directly goto the else loop. 
for a in i:
    print("it is in for loop")
else:
    print("it is in else part")


##The for ... else statement is used to implement search loops.

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
