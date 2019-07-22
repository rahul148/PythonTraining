#set
my_set={1,3,2}
print(my_set)

myset={1,'hello',(1,2,3)}
print(myset)

#convert the list into set
myset=set([1,2,3])
print(myset)

#intialize the set()
a=set()
print(type(a))

#operations
myset1={1,3}
print(myset1)

#add only  elements
myset1.add(32)
print(myset1)

#update-using
myset1.update([11,1],{22,55})
print(myset1)

#remove
myset1.remove(32)#it show error when element not persent in the list
print(myset1)

myset1.discard(32)#if the element is not persent in set and you delete that element it does not show the error
print(myset1)

a={1,2,3,4}
b={2,3,4,5}
uni=a.union(b)
print(uni)
uni=a.intersection(b)
uni=a-b#a.difference(b)
print(uni)


m=max(a)
print(m)
m=min(b)
print(m)

print(a.clear())





#itearation
b={8,9,5,6,8}
for i in b:
    print(i)
c=sorted(b)
print(c)


 


