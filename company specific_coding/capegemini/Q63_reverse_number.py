# QUESTION:
# Write a function to reverse the digits of a number.
#
# Example:
# 1234 → 4321
# 507 → 705

def reverse_number(n):
    reverse=0
    digit=0
    while n!=0:
        digit=n%10
        reverse=reverse*10+digit
        n//=10
    return reverse


# TEST CASES
print(reverse_number(1234))  # Expected: 4321
print(reverse_number(507))   # Expected: 705
print(reverse_number(9))     # Expected: 9
print(reverse_number(120))   # Expected: 21