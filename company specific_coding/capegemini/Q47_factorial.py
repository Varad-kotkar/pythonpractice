# QUESTION:
# Write a function to find the factorial of a number.
#
# Example:
# 5 → 120
# 0 → 1


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


# TEST CASES
print(factorial(5))  # Expected: 120
print(factorial(4))  # Expected: 24
print(factorial(1))  # Expected: 1
print(factorial(0))  # Expected: 1