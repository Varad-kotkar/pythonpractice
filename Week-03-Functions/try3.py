try:
    num=int(input("enter first no:"))
except Exception as e:
    print(e)
else:
    square =num*num
    print(square)
finally:
    print("Program Finished")