class student:
    def __init__(self,n,m1,m2,m3):
        self.name=n
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    def avg(self):
        return (self.marks1+self.marks2+self.marks3)/3
name=str(input("Enter the name of student:"))
s1=int(input("enter marks of chem:"))
s2=int(input("enter marks of phy:"))
s3=int(input("enter marks of math:"))

s=student(name,s1,s2,s3)
print("the avg marks of student is::",s.avg())
