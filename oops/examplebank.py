class bank():
    def __init__(self,name,accno,amount):
        self.name=name
        self.accno=accno
        self.amount=amount
        print("account is create")
    
    def display(self):
        print("\nAccount Details.....")
        print("Name:",self.name)
        print("account no:",self.accno)
        print("amount account:",self.amount)
    def deposit(self,amount):
        if(self.amount>5000):
            self.amount+=amount
            print("update amount",self.amount)
        else:
            print("Not deposite any thing.....")
    def withdraw(self,d):
        if (self.amount<5000):
            print("balance is insufficient")
        else:
            self.amount=self.amount-d
            if(self.amount<5000):
                print("unble to withdraw")
            else:
                self.amount=self.amount-d
                print("remaining amount",self.amount)
            #print("\nAvailabe balance",self.amount)


print("required information for create account...")
name=str(input("enter the name: "))
accno=int(input("enter the account number to open:"))
amt=int(input("enter the amount:"))
if amt<5000:
    print("unble to create account minimum required is 5000.... ")
else:
    b=bank(name,accno,amt)
    b.display()
    amount=int(input("\nenter the amount to deposite:"))
    b.deposit(amount)
    d=int(input("\nenter the amount do you want withdraw:"))
    b.withdraw(d)
