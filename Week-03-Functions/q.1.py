'''Write a program that:

Opens the file using with.
Reads the contents.
Converts the contents into a list using split("\n").
Builds a frequency dictionary.
Prints the frequency of each student.'''
with open("students.txt") as f:
    read=f.read()
    students= read.split("\n")
    freq={}
    for i in students:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
