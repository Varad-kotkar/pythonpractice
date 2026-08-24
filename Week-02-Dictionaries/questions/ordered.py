'''students = [
    "Rahul",
    "Varad",
    "Rahul",
    "Amit",
    "Viraj",
    "Amit",
    "Rahul",
    "Rohan"
]
Requirement
Print every student exactly once, in the order they first appeared.'''

attendance = [
    "Rahul",
    "Varad",
    "Rahul",
    "Amit",
    "Viraj",
    "Amit",
    "Rahul",
    "Rohan"
]

once= set()
for i in attendance:
    if i not in once:
        once.add(i)
        # if i in once:
        print(i)



    