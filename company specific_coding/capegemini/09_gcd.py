# QUESTION:
# Write a program to find the GCD (Greatest Common Divisor)
# of two given numbers.
#
# Example:
# 12 and 18
# Common divisors: 1, 2, 3, 6
# GCD = 6


a = 12
b = 18
if a>b:
    c=b
else:
    c=a

gcd=0
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        gcd=i

print(gcd)




# TEST CASES
# 12, 18 → Expected: 6
# 15, 25 → Expected: 5
# 7, 13  → Expected: 1
# 20, 8  → Expected: 4