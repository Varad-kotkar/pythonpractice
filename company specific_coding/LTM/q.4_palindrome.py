n=input("Enter the word")
r=""
for i in n:
    r=i+r
if r==n:
    print("palindrome")
else:
    print("Non Palindrome")