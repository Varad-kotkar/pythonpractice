# QUESTION:
# Write a program to print the first n terms of the Fibonacci series.
#
# Fibonacci series:
# 0 1 1 2 3 5 8 13 ...
#
# Each number is the sum of the previous two numbers.


n = 7
fibonaci=0
a=0
b=1
if n==1:
    print(a)
else:
    print(a)
    print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c

    print(c)




# EXPECTED OUTPUT:
# 0 1 1 2 3 5 8