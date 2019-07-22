class student:
    """def __init__(self,name=None,age=None):
        self.name=name
        self.age=age"""
    def studdetails(self):
        if self.name or self.age:
            print("student info:"+self.name,self.age)
        else:
            ("no information available")
    def set_info(self,name,age):
        self.name=name
        self.age=age
x=student()
x.set_info("rahul",10)
x.studdetails()
