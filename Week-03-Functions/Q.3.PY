'''🎯 Challenge (Placement Level)

Now write a program for this file:

marks.txt

85
92
78
65
99
Requirements
Open the file.
Use:
for line in f:
Convert every line to an integer.
Calculate:
Total marks
Average marks
Highest mark
Lowest mark
Expected Output
Total Marks: 419
Average Marks: 83.8
Highest Marks: 99
Lowest Marks: 65'''
Total_marks=0
# highest=0
highest = None
lowest = None
count=0
with open ("marks.txt",'r') as f:
    for line in f:
        line=int(line.strip())
        Total_marks=Total_marks+line
        count+=1
        if highest is None or line >highest:
            highest=line
        # avg_marks=Total_marks/count
        if lowest is None or line < lowest:
            lowest=line
avg_marks=Total_marks/count



print(Total_marks)
print(avg_marks)
print(highest)
print(lowest)
    
