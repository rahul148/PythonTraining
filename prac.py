a=100
print(hex(a))
b=200

c=a>b
print(c)#it show thw boolen(true,false) values 

s={10,2,0,3,'durga'}#set is used to display the unoredered elements
                    #its remove the duplicates values
print(s)
print(type(s))
fs=frozenset(s)#f=definiation of forzenset same as set but its immutable
print(fs)

###dictionary
d={1:'rahul',2:'3',3:'4'}
print(d)
for i in d:
    print(d)
a=10
b=10
print(a is b)

a="durga"
b="durga"
print(id(a))
print(id(b))
print(a is b)
#We can use "is" operator for address comparison where
#as == operator for content(values) comparison1
