new_student=input("enter new students : ")
with open ('students.txt','a') as f:
    f.write("\n" + new_student)

with open ('students.txt','r') as f:
    print(f.read())