'''Retry Password

Write a program that:

The correct password is:
password = "python123"
Ask the user to enter the password.
If it is incorrect:
Incorrect password.
Keep asking until the correct password is entered.
When correct:
Login Successful
Additional Requirement

If the user enters an empty password:

""

use:

raise ValueError("Password cannot be empty.")
Requirements
while True
try
raise
except ValueError
else
break'''
while True:
    try:
        password=str(input("enter the password : "))
        if password =="":
            raise ValueError("Password cannot be empty.")
        elif password !="python123":
            raise ValueError("Incorrect password.")
        
    except ValueError as e:
        print(e)
    else:
        print("Login Successful")
        break
    
