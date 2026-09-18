# QUESTION:
# Write a function to check whether a given number is a Perfect Number.
#
# A Perfect Number is a number whose proper divisors
# add up to the number itself.
#
# Example:
# 6 → divisors: 1, 2, 3
# 1 + 2 + 3 = 6
# Therefore, 6 is a Perfect Number.


def is_perfect(n):
    perfect_no=0
    for i in range(1,n):
        if n%i==0:
            perfect_no+=i
    return perfect_no == n
    # if perfect_no==n:
    #     return True
    # else:
    #     return False


# TEST CASES
print(is_perfect(6))    # Expected: True
print(is_perfect(28))   # Expected: True
print(is_perfect(12))   # Expected: False
print(is_perfect(1))    # Expected: False