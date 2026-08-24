'''Employee Salary Calculator

A file named salary.txt contains one salary per line.

Example 1:

50000
45000
60000
55000

Your program should calculate and print:

Average Salary = 52500.0
But your program must also handle these cases:
Case 1: File doesn't exist

Output:

Salary file not found.
Case 2: Invalid data

Example:

50000
abc
45000

Output:

Invalid salary data found.
Case 3: Negative salary

Example:

50000
-1000
45000

Negative salary is not allowed.

Use:

raise ValueError("Salary cannot be negative.")
Case 4: Empty file

If the file has no salaries:

Output:

No salary records found.
Requirements

Your solution should use:

✅ with open()
✅ while is not required
✅ try
✅ except FileNotFoundError
✅ except ValueError
✅ else
✅ raise
✅ Calculate the average only once, after reading all salaries'''
count=0
total_salary=0
    try :
        with open ("salary.txt","r") as f:
        data=f.readlines()

        for salary in data:
            salary=int(salary)
            if salary is not int:
                raise ValueError("Invalid salary data found.")
            if salary<0:
                raise ValueError("Salary cannot be negative.")
            count+=1
            total_salary+=salary
        if count==0:
            raise ValueError("No salary records found.")

    except FileNotFoundError:
        print("Salary file not found.")
    except ValueError as e:
        print(e)
    else:
        avg_salary=total_salary/count
        print(avg_salary)

