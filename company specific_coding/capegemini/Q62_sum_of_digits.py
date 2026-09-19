# QUESTION:
# Write a function to find the sum of all digits of a number.
#
# Example:
# 1234 → 10
# 507 → 12


def sum_of_digits(n):
    total=0
    digit=0
    while n!=0:
        digit=n%10
        total+=digit
        n//=10
    return total

# TEST CASES
print(sum_of_digits(1234))  # Expected: 10
print(sum_of_digits(507))   # Expected: 12
print(sum_of_digits(9))     # Expected: 9
print(sum_of_digits(100))   # Expected: 1