class BankAccount:
    def __init__(self,name,balance=0):
        self.account_holder = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} to your account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("not enough balance")
        else:
            self.balance = self.balance - amount
    def __str__(self):
        return f"AccountHolder Name:{self.account_holder} \n Balnce:{self.balance}"
obj = BankAccount("Ramesh", 10000) 
print(obj)
obj.deposit(2000)
obj.withdraw(1000)
print(obj)