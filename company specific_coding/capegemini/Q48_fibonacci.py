# QUESTION:
# Write a function to return the first n Fibonacci numbers.
#
# Example:
# n = 6 → [0, 1, 1, 2, 3, 5]


def fibonacci(n):
    fibo=[]
    a=0
    b=1
    if n==1:
        fibo.append(a)
    else:
        fibo.append(a)
        # fibo.append(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            fibo.append(c)
    return fibo


# TEST CASES
print(fibonacci(6))  # Expected: [0, 1, 1, 2, 3, 5]
print(fibonacci(5))  # Expected: [0, 1, 1, 2, 3]
print(fibonacci(1))  # Expected: [0]
print(fibonacci(0))  # Expected: []