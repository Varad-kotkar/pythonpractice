try :
    num=int(input("enter first no:"))
    square= num *num
    print(f"square:{square}")
except ValueError:
    print("Invalid integer!")