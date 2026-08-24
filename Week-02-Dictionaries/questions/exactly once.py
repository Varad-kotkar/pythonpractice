'''A school records student attendance.

attendance = [
    "Rahul",
    "Varad",
    "Rahul",
    "Amit",
    "Viraj",
    "Amit"
]

Requirement:

Print only students who attended exactly once.'''

attendance = [
    "Rahul",
    "Varad",
    "Rahul",
    "Amit",
    "Viraj",
    "Amit"
]

students={}
for  std in attendance:
    if std not in students:
        students[std]=1
    else:
        students[std]+=1

for key,values in students.items():
    if values == 1:
        print(key)


# once=set()
# for a in attendance:
#     once.add(a)
#     once= once.symmetric_difference(attendance)
# print(once)
