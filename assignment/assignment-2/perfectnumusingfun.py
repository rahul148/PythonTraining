def per(start,end):
    for i in range(start,end+1):

        sum=0
        for j in range(1,i):
            if(i%j==0):
               sum=sum+j
               if(sum==i):
                   print(i,"is perfect number")
per(1,2000)
