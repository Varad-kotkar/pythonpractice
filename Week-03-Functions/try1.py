# try:
#     num1=int(input("enter first no:"))
#     num2=int(input("enter sec no:"))
#     result= num1/num2
#     print(f"result=",{result})
# except Exception as e:
#     print(e)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter valid integers.")
try:
    print("A")
    x = int("abc")

except Exception:
    print("B")

except ValueError:
    print("C")

print("D")