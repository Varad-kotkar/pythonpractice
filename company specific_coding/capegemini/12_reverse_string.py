# QUESTION:
# Write a function to reverse a given string.
#
# Example:
# Input: "hello"
# Output: "olleh"


def reverse_string(s):
    return s[::-1]

# def reverse_string(s):
#     s=s.split()
#     for i in s:
#         if i==
# TEST CASES
print(reverse_string("hello"))      # Expected: olleh
print(reverse_string("python"))     # Expected: nohtyp
print(reverse_string("abc"))        # Expected: cba
print(reverse_string("a"))          # Expected: a