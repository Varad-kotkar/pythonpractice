'''Write a program that:
Ask the user for marks.
Marks must be between 0 and 100.
If the user enters:
text → "Invalid input!"
less than 0 → "Marks cannot be negative."
greater than 100 → "Marks cannot exceed 100."
If valid:
Grade Stored Successfully
Requirements
while True
try
raise
except
else
break'''
while True:
    try:
        marks=int(input("Enter marks : "))
        if marks <0:
            raise ValueError("Marks cannot be negative.")
        if marks >100:
            raise ValueError("Marks cannot exceed 100.")
    # except Exception as e:
    except ValueError as e:
        print(e)
    else:
        print("Grade Stored Successfully")
        break


