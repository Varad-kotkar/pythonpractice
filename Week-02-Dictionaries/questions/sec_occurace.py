'''orders = [
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Monitor",
    "Headphones"
]

Requirement:

Print each repeated product only when it becomes repeated.'''

orders = ["Laptop","Mouse","Laptop","Keyboard","Mouse","Monitor","Monitor","Headphones"]
seen = set()
printed = set()

for i in orders:
    if i not in seen:
        seen.add(i)
# for i in orders:
    elif i in seen:
            if i not in printed:
                printed.add(i)
                print(i)
    