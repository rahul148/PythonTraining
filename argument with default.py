def func(i,j=10):
    print(i,j)
func(2)
func(1,3)#if you pass the value the default value is not consider

def fun(a,b):
    if a>b:
        return a,b
