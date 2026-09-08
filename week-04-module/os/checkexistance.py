import os

if os.path.isfile("students.txt"):
    print("It is a file")
elif os.path.isdir("students.txt"):
    print("It is a directory")


else:
    print("Does not exist")


