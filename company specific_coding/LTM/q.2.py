# QUESTION:
# Write a Python program to print the first n numbers
# of the Fibonacci series.
#
# In the Fibonacci series, each number is the sum
# of the previous two numbers.
#
# Example:
# Input: 7
# Output: 0 1 1 2 3 5 8
#
# TEST CASES:
# Input: 5
# Expected: 0 1 1 2 3
#
# Input: 1
# Expected: 0
#
# Input: 2
# Expected: 0 1
n= int(input("Enter the number"))

# fibonaci=1
# for i in range(1,n+1):
#     fibonaci*=i
# print(fibonaci)

a=0
b=1
if n==1:
    print (a)
else:
    print(a)
    print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)