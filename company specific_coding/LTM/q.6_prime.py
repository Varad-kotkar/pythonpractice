n = int(input("enter no"))
prime=True
# n = int(input("Enter number: "))

if n<=1:
    print("Not prime")
else:
    
    for i in range(2,n//2+1):
        if n %i==0:
            prime=False
            break
        # else:
        #     prime=True
    # print(prime)
    if prime==True:
        print("Num is prime")
    else:
        print("Num is not prime")