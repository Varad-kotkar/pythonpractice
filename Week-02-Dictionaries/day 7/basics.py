'''Problem 1 (Easy)

Create a dictionary storing:

Name
Age
Branch

Print all three values.'''


student={"name":"varad","Age": 21, "Branch":"cse"}
# print(student["Age","Branch ","name"])
print(student["Age"])
print(student["name"])
print(student["Branch"])
a=student.items()
print(a)
print(len(student))
print(student.get("Age"))