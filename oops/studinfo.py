class stud:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age
    def studinfo(self):
        self.name=str(input("enter the name\n"))
        self.age=int(input("enter the age"))
    def display(self):
        print(self.name)
        print(self.age)
s=stud()
s.studinfo()
s.display()
