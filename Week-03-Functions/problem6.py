'''ATM Withdrawal

Initial balance:

balance = 5000

Program should:

Ask user for withdrawal amount.
If user enters text:
abc

print

Invalid amount!
If amount is negative:
Withdrawal amount cannot be negative.
If amount is greater than balance:
Insufficient balance.
Otherwise:
Withdrawal successful.

Remaining Balance = ...
Requirements
while True
try
except
raise
else
break

💡 Hint: Use raise ValueError(...) for the negative amount. Don't create a custom exception yet—we'll keep it simple.'''

# balance = 5000
# # class Exception:
# #     pass
# try :
#     amt=int(input("Enter the Amount : "))
#     final= balance-amt
#     print(final)
#     print("Withdrawal successful.")
#     if amt<0:
#         raise TypeError
#     if amt > balance:
#         raise FileNotFoundError
# except ValueError:
#     print("Invalid amount!")
# except TypeError:
#     print("Withdrawal amount cannot be negative.")
# except FileNotFoundError:
#     print("Insufficient balance.")
balance = 5000

while True:
    try:
        amt = int(input("Enter amount: "))

        if amt < 0:
            raise ValueError("Withdrawal amount cannot be negative.")

        if amt > balance:
            raise ValueError("Insufficient balance.")

    except ValueError as e:
        print(e)

    else:
        balance -= amt
        print("Withdrawal successful.")
        print(f"Remaining Balance = {balance}")
        break