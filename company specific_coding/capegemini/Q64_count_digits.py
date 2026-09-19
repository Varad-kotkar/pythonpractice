# QUESTION:
# Write a function to count the number of digits in a number.
#
# Example:
# 12345 → 5
# 7 → 1
# 100 → 3


def count_digits(n):
    count=0
    digit=0
    if n==0:
        return 1
    while n!=0:
        digit=n%10
        count+=1
        n//=10
    return count


# TEST CASES
print(count_digits(12345))  # Expected: 5
print(count_digits(7))      # Expected: 1
print(count_digits(100))    # Expected: 3
print(count_digits(0))      # Expected: 1