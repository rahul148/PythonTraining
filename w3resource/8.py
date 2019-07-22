import numpy
#python progrma to display first n last element from list
list1=["red","white","blue"]
print(list1[0::2])#it show the last and first element
print("%s %s"%(list1[0],list1[2] or list[-1]))
#print examination date
exam_date=(10,3,2019)
print("%i/ %i / %i"%(exam_date))


#add number input(n)=o/p:n+nn+nnn
n=int(input("enter the value:"))
n1=int("%s" % n)
n2=int("%s%s"% (n,n))
n3=int("%s%s%s"% (n,n,n))
print(n1+n2+n3)

#Write a Python program to print the documents (syntax, description etc.)
#of Python built-in function(s).
print(abs.__doc__)

