#create the list-list is created by using square brackets[]
#1)create list with smiler data type list or different data type
list1=[1,2,3,4,5]
print(list1)

# Error! Only integer can be used for indexing
# list1[4.0]

list2=["a","b","c"]
print(list2)
list3=["a",1,"b",3]
print(list3)
#list[0]-it print the value at index zero
print(list1[0])
#list[-1]-it print the number from reverse side starting index is -1
print(list2[-1])
#silcing of elements in the list-start index is zero so it will print 3
print(list3[0:3])
#reverse slicing is not possible in single list
print(list1[-1:0])#its show the empty list in output

#Add element in list by using +
"""
We can also use + operator to combine two lists.
This is also called concatenation."""
list1=[1,2,3]
new=[6,7,8]
list1=list1+new
print(list1)

#using"*"multiply sign you can print the elements of list multipe time
list4=[1,2,3]*3
print(list4)

####nested list#####
list5=[1,2,3,["a","b"]]
print(list5)

print(list5[0])#print from the nested list the list at index 0.
print(list5[1])

#nested indexing
list5=[123,33,[1,2,3]]
print(list5[1])

list6=["happy",[1,2,3]]
print(list6[0][1])#this print output "a"

print(list6[1][1])#it print o/p is "2"


##########python Built-in Functions###########


### some important opertions on list###
#1]Append-it append only one at the end element to list
mylist=[1,2,3]
mylist.append(5)
print(mylist)

#2)clear
mylist.clear()#its make empty lit or clear/delete all elementd from the list
print(mylist)

#3] copy-its on;y copy from one to another
mylist=[1,2,3]
newlist=mylist.copy()
print(newlist)

#4]count-its show the elements are occurce how many times in list
mylist=[7,8,9,7,1,7]
print(mylist.count(7))

#5]extend-its add the multiple elements into exits list or extend the list
m=[11,22,33]
m.extend([7,8,9])
print(m)
    #test cases====>
    ##--1)m.extend()=TypeError: extend() takes exactly one argument (0 given)

#6]index

"""-In simple terms, index() method finds the given element in
a list and returns its position.

However, if the same element is present more than once,
index() method returns its smallest/first position."""
l=[1,2,3,4,"R"]
find=l.index(1)#find the 1 from the list and return index values

print(find)
find1=l.index("R")
print(find1)

#7)insert
"""The insert() function takes two parameters:

index - position where an element needs to be inserted
element - this is the element to be inserted in the list
syntax:
list.insert(indexno,value)"""

l2=[1,2,3]
l2.insert(2,10)
print(l2)

#8)pop
"""
The pop() method takes a single argument (index) and
removes the item present at that index.

If the index passed to the pop() method is not in range,
it throws IndexError: pop index out of range exception.

The parameter passed to the pop() method is optional.
If no parameter is passed, the default index -1 is passed as
an argument which returns the last item.

#####Return Value from pop()
The pop() method returns the item present at the given index. This item will be removed the list.
"""

l2.pop(1)
print(l2)

#9)remove
"""
The remove() method removes the item which is passed as an argument.

If you need to delete elements based on the index (like the fourth element or last element),
you can use the pop() method. Also,
you can use del statement to remove items from a list or
delete an entire list.
"""
l2.remove(10)
print(l2)

#Python List reverse()
"""
The syntax of reverse() method is:

list.reverse()
The reverse() function doesn't return any value.
It only reverses the elements and updates the list.
"""
r=["a","b","c"]
print("before reverse:",r)
r.reverse()
print("after reverse:",r)

#sort
"""By default, sort() doesn't require any extra parameters.
However, it has two optional parameters:

reverse - If true, the sorted list is reversed
(or sorted in Descending order)
key - function that serves as a key for the sort comparison
"""

rahul=[1,2,3,50,11,20]
rahul.sort()#by defult it ssort the list in ascending order 
print(rahul)
"""a=["c","d","f",3,2,1]
a.sort()-TypeError: '<' not supported between instances of 'int' and 'str'
print(a)"""

#for descending order
rahul.sort(reverse=True)
print(rahul)


