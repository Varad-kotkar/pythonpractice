'''An online store records products viewed.

views = [
    "Mouse",
    "Keyboard",
    "Mouse",
    "Laptop",
    "Monitor",
    "Laptop"
]

Requirement

Show every unique product viewed.'''

views = [
    "Mouse",
    "Keyboard",
    "Mouse",
    "Laptop",
    "Monitor",
    "Laptop"]


students={}
for  std in views:
    if std not in students:
        students[std]=1
    else:
        students[std]+=1

for key,values in students.items():
    if values == 1:
        print(key)


# unique=set()
# for a in views:
#     unique.add(a)
# print(unique)GGG