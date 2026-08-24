import json

student = {
    "name": "Varad",
    "age": 21,
    "skills": ["Python", "SQL"]
}

with open("student.json", "w") as f:
    json.dump(student, f)

data=json.dumps(student) 
print(data) 
print(type(data))