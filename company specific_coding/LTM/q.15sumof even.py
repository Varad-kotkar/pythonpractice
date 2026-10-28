arr=list(map(int,(input("enter arr: ").split())))
total=0
for num in arr:
    if num%2==0:
        total+=num

print(total)
