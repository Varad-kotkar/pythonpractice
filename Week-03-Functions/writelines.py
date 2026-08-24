# students = [
#     "Rahul\n",
#     "Varad\n",
#     "Amit\n",
#     "Neha\n"
# ]
students = ["Rahul", "Varad", "Amit", "Neha"]
with open ('students.txt','w') as f:
    # f.writelines(students)
    for line in students:
        f.write(line)
        f.write("\n")

with open ('students.txt','r') as f:
    print(f.read())