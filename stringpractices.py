n=str(input("enter the string :"))
m=len(n)
m=n[1:7:]
print(m)
m=n[::-1]
print(m)

s="rahul"

print("forword direction")

for i in s:
    print(i,end='')

print("backword direction")
for i in s[::-1]:
    print(i,end=' ')
