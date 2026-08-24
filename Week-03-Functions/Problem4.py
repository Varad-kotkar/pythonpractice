'''Given:

student_marks = {
    "Rahul": 85,
    "Varad": 92,
    "Amit": 78
}

Write a program that:

Asks the user for a student name.
Prints the student's marks.
If the student doesn't exist, print:
Student not found!
Keep asking until a valid student name is entered.
Example
Enter student name: Neha
Student not found!

Enter student name: Rahul
Marks = 85
Requirements
while True
try
except
else
break'''

student_marks = {
    "Rahul": 85,
    "Varad": 92,
    "Amit": 78
}
while True:
    try:
        name = str(input("Enter the name of student : "))
        # print(student_marks.key(name))
        print(f"Marks = {student_marks[name]}")

        # for name in student_marks.items():
        #         print(f"marks of {name} is : {name}")
        # for key,value in student_marks.items():
        #     if name in student_marks.items():
        #         print(f"marks of {name} is : {key}")
    except KeyError:
        print("Student not found!")
    else:
        break

