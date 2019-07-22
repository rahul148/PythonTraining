def length(t):
    count=0
    for i in t:
        count=count+1
        print(i)
    return count
t=(1,2,3)
result=length(t)
print(result)
#you can update the element of list which is declear inside the tuples
t1=(1,2,3,[22,33])
t1[3][0]=44
print(t1)
#o/p :(1, 2, 3, [44, 33])
