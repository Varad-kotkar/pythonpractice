age = int(input("Enter age: "))
try:
    if age < 18:
        raise ValueError("Age must be at least 18.")
except Exception as e:
    print(e)
else:
    print("Access Granted")


