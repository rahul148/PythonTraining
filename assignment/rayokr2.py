def pair(arr,arr_size,sum):

    s=set()

    for i in range(0,arr_size):
        temp=sum-arr[i]
        if(temp>=0 and temp in s):
            print("pair with given sum is:",arr[i],"and",temp)
        s.add(arr[i])

A=[10,0,-1,20,25,30]
n=45
pair(A,len(A),n)
#output-
#pair with given sum is: 25 and 20
