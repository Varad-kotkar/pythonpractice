# QUESTION:
# Write a function to check whether a given number is a Prime Number.
#
# A prime number has exactly two factors: 1 and itself.
#
# Return True if the number is prime, otherwise return False.


def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n% i==0 or n<=0 :
            return False
    else:
        return True


# TEST CASES
print(is_prime(7))    # Expected: True
print(is_prime(10))   # Expected: False
print(is_prime(2))    # Expected: True
print(is_prime(1))    # Expected: False
print(is_prime(17))   # Expected: True
print(is_prime(0))   # Expected: True