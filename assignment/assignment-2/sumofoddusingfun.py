def odd(max):
    oddtotal=0
    num=1
    while num<= max:
        if(num%2!=0):
            oddtotal=oddtotal+num
        num=num+1
    return oddtotal
    
oddtotal=odd(500)

print("sum of odd num:",oddtotal)

