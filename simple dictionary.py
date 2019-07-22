#dictionary
dict1={1:'rahul',2:"rahul"}
print(dict1)
num={1,2,3,4}
item={"rahul"}

item=dict.fromkeys(num,item)
print(item)

dict2={1:"mango",2:"apple",3:"banana"}
print(dict2)

print(dict2.pop(2))#its use to remove the particular keyvalues
print(dict2)

print(dict2.get(3))
print(dict1.popitem())#its pop and remove last item from list

print(dict1)
dict1.clear()#its empty/delete all item from the dictionary but srtucture of dictionary is remain 

print(dict1)
del dict1

#print(dict1)
"""after using del dict1
  print(dict1)
NameError: name 'dict1' is not defined"""



dict2[4]="pune"#its add item in last into dictionary 
print(dict2)

del dict2[4]
print(dict2)#it delete the particular item from dictionary
