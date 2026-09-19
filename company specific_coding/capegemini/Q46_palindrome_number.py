# QUESTION:
# Write a function to check whether a number is a palindrome.
#
# A palindrome reads the same forward and backward.
#
# Example:
# 121 → True
# 123 → False


def is_palindrome_number(n):
    reverse=0
    original=n
    while True:
        digit=n%10
        reverse=reverse*10+digit
        n//=10
        if n==0:
            break
    return reverse==original
#or
    return str(n)==str(n)[::-1]




# TEST CASES
print(is_palindrome_number(121))   # Expected: True
print(is_palindrome_number(123))   # Expected: False
print(is_palindrome_number(1221))  # Expected: True
print(is_palindrome_number(10))    # Expected: False