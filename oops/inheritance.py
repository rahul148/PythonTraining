#inheritance
class car:
    def changegear(self):
        print("old gear system")
    def updatemodel(self):
        print("this updatable version of car")
class bmw(car):
    def auto(self):
        print("new car")
    
    
b=bmw()
b.auto()
d=car()
d.changegear()
d.updatemodel()
