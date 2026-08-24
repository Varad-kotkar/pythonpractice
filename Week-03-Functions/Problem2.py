'''Write a program that:

Keeps asking for two integers.
If either input is invalid, show:
Invalid input. Try again.
If the second number is 0, show:
Cannot divide by zero.
If everything is correct:
Result = 5.0

and exit the loop.

Example
Enter first number: abc
Invalid input. Try again.

Enter first number: 10
Enter second number: 0
Cannot divide by zero.

Enter first number: 10
Enter second number: 2
Result = 5.0'''

try:
    num1=int(input("enter first no"))
    num2=int(input("enter sec no"))
    result= num1/num2
    print(f"result:{result}")
except ValueError:
    print("Invalid input. Try again.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
