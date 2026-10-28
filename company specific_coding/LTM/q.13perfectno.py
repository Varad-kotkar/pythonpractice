n = int(input("Enter number: "))
addition=0
for i in range(1,n):
    if n%i==0:
        addition+=i
print(addition)
print(addition==n)