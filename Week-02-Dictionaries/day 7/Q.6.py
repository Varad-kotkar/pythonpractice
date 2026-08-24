student = {
    "name": "Varad",
    "age": 21,
    "branch": "CSE"
}
for  i in student.values():
     print(i)


for key,value in student.items():
    print(value)


print(len(student.values("Varad")))