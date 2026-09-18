# QUESTION:
# Write a program to check whether a given number is a Palindrome.
#
# A palindrome reads the same forward and backward.
#
# Example:
# 121 → Palindrome
# 123 → Not Palindrome


n =121
original = n
reverse=0
while (n!=0):
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print(reverse)
if original==reverse:
    print(True)
else:
    print(False)
# TEST CASES
# 121 → Expected: Palindrome
# 123 → Expected: Not Palindrome
# 1221 → Expected: Palindrome
# 12321 → Expected: Palindrome