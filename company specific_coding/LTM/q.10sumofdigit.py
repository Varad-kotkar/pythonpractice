n = int(input("Enter number: "))
original=n
total=0
while n!=0:
    digit=n%10
    total+=digit
    n//=10
print(total)