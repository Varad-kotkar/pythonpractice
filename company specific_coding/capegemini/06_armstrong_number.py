# QUESTION:
# Write a program to check whether a given number is an Armstrong number.
#
# For a 3-digit number:
# Sum of the cubes of its digits = the original number.
#
# Example:
# 153 = 1³ + 5³ + 3³ = 153
#
# Return/print True if it is an Armstrong number, otherwise False.


n = 123
cube=0
for i in (str(n)):
    cube+=int(i)**3
if cube==n:
    print(True)
else:
    print(False)
print(cube)


# TEST CASES
# 153 → Expected: True
# 370 → Expected: True
# 123 → Expected: False
# 407 → Expected: True