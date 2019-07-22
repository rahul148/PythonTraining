#overloading
class point:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __str__(self):
        return "({0},{1})".format(self.a,self.b)
    def __add__(self,other):#its add method for overloading
        x=self.a+other.a
        y=self.b+other.b
        return point(x,y)
p1=point(2,3)
p2=point(-1,2)
p3=p1+p2
print("p3=",p3)
