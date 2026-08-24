with open('subjects.txt','r') as f:
    subjects=f.readlines()
total_subjects=len(subjects)
print(f"The complete list:{subjects[:]}")
print(f"The first subject:{subjects[0]}")
print(f"The last subject:{subjects[-1]}")
print(f"The total number of subjects:{}")


with open("subjects.txt", "r") as f:
    for line in f:
        print(line)