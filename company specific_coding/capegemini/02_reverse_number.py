# QUESTION:
# Write a program to reverse a given number.
#
# Example:
# Input: 12345
# Output: 54321


# TEST CASES
n = 12300
reverse=0
while (n!=0):
    digit =(n%10)
    reverse=reverse*10+digit
    n//=10
print(reverse)






# Expected Output:
# 54321