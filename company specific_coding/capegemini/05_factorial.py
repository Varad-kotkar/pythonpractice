# QUESTION:
# Write a program to find the factorial of a given number.
#
# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120


n = 5
fact=1
for i in range(1,n+1):
    fact*=i

print(fact)
    


# TEST CASES
# 5 → Expected: 120
# 4 → Expected: 24
# 1 → Expected: 1
# 0 → Expected: 1