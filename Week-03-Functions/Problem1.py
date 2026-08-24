'''Write a program that keeps asking the user for an integer until they enter a valid one.

Example:

Enter an integer: abc
Invalid input. Try again.

Enter an integer: 12

You entered: 12
Rules
Use while True
Use try
Use except ValueError
When a valid number is entered, print it and exit the loop using break.'''

while True:
    try:
        num=int(input("Enter an integer:"))
    except ValueError:
        print("Invalid input. Try again.")
    else:
        print(f"NUM:{num}")
        break

