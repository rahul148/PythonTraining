def ser(num):
    res=0
    fact=1

    for i in range(1,num+1):
        fact=fact*i
        res=res+(fact//i)
    return res
n=int(input("enter the numbe"))
result=ser(n)
print("sum of factorial series 1 to n",result)
