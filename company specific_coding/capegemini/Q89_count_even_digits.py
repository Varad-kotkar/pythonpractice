# QUESTION:
# Write a function to count how many even digits are present
# in a number.
#
# Example:
# 123456 → 3
# 2468 → 4
# 1357 → 0


def count_even_digits(n):
    count=0
    while n!=0:
        digit=n%10
        if digit %2==0:
            count+=1
        n//=10
    return count




# TEST CASES
print(count_even_digits(123456))  # Expected: 3
print(count_even_digits(2468))    # Expected: 4
print(count_even_digits(1357))    # Expected: 0