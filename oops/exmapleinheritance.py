class person:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last
    def getName(self):
        return  self.firstname+""+self.lastname
    def __str__(self):#its convert to string and pass to derived class5
        return self.firstname+""+self.lastname
class employee(person):
    def __init__(self,first,last,empid):
        super().__init__(first,last)
        self.empid=empid
    def getemp(self):
        return self.getName()+","+self.empid
x=person("rahul","shinde")
y=employee("rahul","shindeee",'1001')
print(x.getName())
print(y.getemp())
print(x)
print(y)
