n=int(input())
if n<=1:
    print(False)
prime=True
for i in range(2,n//2+1):
    if n%i==0:
        prime=False

print(prime)
        