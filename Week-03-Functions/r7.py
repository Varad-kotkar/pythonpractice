class BankAccount:
    def __init__(self, owner,balance):  
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        return self.balance+=amount

    def withdraw(self,amount):
        if self.balance <amount:
            print("Insufficient Balance")
        else:
            return  self.balance-=amount
    def display(self):
        print(f"Owner:{self.owner}")
        print(f"balance:{self.balance}")


acc = BankAccount("Varad", 5000)

acc.deposit(1000)

acc.withdraw(2000)

acc.display()