n = int(input("Enter number: "))
original=n
count=0
#imp
if n==0:
    print(1)
else:
    while n!=0:
        digit=n%10
        count+=1
        n//=10
    print(count)