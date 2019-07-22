class vehicle:
    def __init__(self,colour,name,prise):
        self.colour=colour
        self.name=name
        self.prise=prise
    def display(self):
        print("\nName:",self.name)
        print("Prise:",self.prise,"\ncolour:",self.colour)
b=vehicle('red','fer',6000000)
b.display()
d=vehicle('Blue','vanjump',1000000)
d.display()
