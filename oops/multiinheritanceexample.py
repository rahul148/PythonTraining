class a:
    def __init__(self,f):
        self.fname=f
        print("in first parent")
    def getname(self):
        return self.fname
class b:
    def __init__(self,l):
        print("second parent")
class derived(a,b):
    def __init__(self,name):
        super().__init__(name)#its call the first parent class
        super().__init__(name)
        b.__init__(self,name)
    
d=derived("rahul")

