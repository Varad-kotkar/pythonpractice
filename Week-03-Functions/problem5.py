'''Suppose the file marks.txt contains:

85
92
78
65
99

Write a program that:

Opens marks.txt.
Reads all marks.
Calculates the average.
Prints:
Average = 83.8

If:

the file doesn't exist → print:
File not found!
the file contains something invalid like:
85
abc
99

print:

Invalid data in file!
Requirements
try
At least two specific except blocks
else'''
try:
    count =0
    total_marks=0
    with open ("marks.txt",'r') as f:
            data=f.readlines()
            for marks in data:
                marks=int(marks)
                count+=1
                avg = total_marks/count
            total_marks+=marks
            print(avg)
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Invalid data in file!")
