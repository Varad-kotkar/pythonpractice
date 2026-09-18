# QUESTION:
# Write a program to find the sum of all digits of a given number.
#
# Example:
# 12345 → 1 + 2 + 3 + 4 + 5 = 15


n = 123
sum=0
while (n!=0):
    digit=n%10
    n//=10
    sum+=digit
print(sum)


# TEST CASES
# 12345 → Expected: 15
# 123 → Expected: 6
# 500 → Expected: 5
# 9 → Expected: 9