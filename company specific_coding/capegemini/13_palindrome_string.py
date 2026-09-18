# QUESTION:
# Write a function to check whether a given string is a Palindrome.
#
# Example:
# "madam" → True
# "hello" → False


def is_palindrome(s):
    reverse=s[::-1]
    return reverse==s


# TEST CASES
print(is_palindrome("madam"))   # Expected: True
print(is_palindrome("hello"))   # Expected: False
print(is_palindrome("level"))   # Expected: True
print(is_palindrome("python"))  # Expected: False