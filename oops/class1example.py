class robot:
    def __init__(self,name=None):#its constructor
        self.name=name
    def say_hi(self):
        if self.name:
            print("hi,i am "+self.name)
        else:
            print("hi am robot without name")
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
x=robot()#invoke constructor(__init__)with parameter
x.set_name("henry")
x.say_hi()
y=robot()#invoke constructor(__init__)without parameter
print(y.get_name())
y.say_hi()
y.set_name("rahul")#invoke constructor(__init__)with parameter
y.say_hi()
print(y.get_name())
