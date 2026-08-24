'''This problem introduces multiple operations inside one try block.

Calculator

Write a program that:

Ask the user for:
First number
Operator (+, -, *, /)
Second number
Perform the operation.
If the operator is not one of the four valid operators, use:
raise ValueError("Invalid operator.")
If the user divides by zero:
Cannot divide by zero.
If the user enters invalid numbers:
Please enter valid integers.
If everything is correct:
Result = ...
Requirements
while True
try
raise
except ValueError
except ZeroDivisionError
else
break'''
operator=["+","-","*","/"]
while True:
    try:
        num1=int(input("Enter First No."))
        opp=input("enter operation : ")
        num2=int(input("Enter Sec No."))
        #Instead of creating four variables use single result
        if opp == "+":
            add= num1+num2
        elif opp =="-":
            sub= num1-num2
        elif opp == "*":
            multi= num1*num2
        elif opp == "/":
            div= num1/num2
        if opp not in operator:
            raise ValueError("Invalid operator.")
        result= add or sub or opp or div 
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"result : {result}")
        break
 