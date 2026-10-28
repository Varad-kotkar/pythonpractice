n = int(input("Enter number: "))
original=n
digit=0
armstrong=0
length=len(str(n))
while n!=0:
    digit=n%10
    armstrong+=digit**length
    n//=10

print(armstrong==original)