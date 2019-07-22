list1=["r","a","a","h","R"]
remove=[]
for i in list1:
    if i not in remove:
        remove.append(i)
print("after removing duplicate values:",remove)
