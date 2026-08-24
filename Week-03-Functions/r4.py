def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount > balance :
        return balance 
    else:
        return balance - amount

def display_balance(balance):
    print(f"Current Balance: {balance}")


balance = 5000

balance = deposit(balance, 1000)

balance = withdraw(balance, 2000)

display_balance(balance)