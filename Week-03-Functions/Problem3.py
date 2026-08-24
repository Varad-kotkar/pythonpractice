'''List Index Access

Given:

numbers = [10, 20, 30, 40, 50]

Write a program that:

Asks the user for an index.
Prints the element at that index.
If the index is out of range, print:
Invalid index!
If the user enters text instead of a number, print:
Please enter a valid integer.
Keep asking until the user enters a valid index.
Example
Enter index: 10
Invalid index!

Enter index: abc
Please enter a valid integer.

Enter index: 2
30
Requirements
while True
try
except ValueError
except IndexError
else
break'''


numbers = [10, 20, 30, 40, 50]

while True:
    try:
        index= int(input("Enter the index to print : "))
        print(numbers[index])
    except ValueError:
        print('Please enter a valid integer.')
    except IndexError:
        print('Invalid index!')
    else:
        break



