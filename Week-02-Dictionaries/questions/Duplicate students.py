students = [
    "Rahul",
    "Amit",
    "Rahul",
    "Varad",
    "Amit",
    "Neha",
    "Varad"
]
'''Requirement

Print

Duplicate students:
Rahul
Amit
Varad'''
unique =set(students)
seen = set()
printed = set()

for i in students:
    if i not in seen:
        seen.add(i)
    elif i in seen:
            printed.add(i)
print(printed)