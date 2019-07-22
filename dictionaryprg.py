dict1={1:'rahul',3:4,2:'ganesh'}
print(dict1)
print(dict1[1])
print(dict1.items())#print the hole dictionary with values
#following is function which print ascending order
p=sorted(dict1.items())
print(p)
#following is function which print dscending order
p=sorted(dict1.items(),reverse=True)
print(p)

dict1.update({5:'jesuslove',6:'balaji'})#for update the multiple values
print(dict1)

print(dict1.pop(3))#it remove the items from dictionary
print(dict1)

