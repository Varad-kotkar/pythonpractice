# QUESTION:
# Write a function to find the LCM (Least Common Multiple)
# of two given numbers.
#
# Example:
# 12 and 18 → LCM = 36


def find_lcm(a, b):
    if a>b:
        c=b
    else:
        c=a
    for num in range(c,a*b+1):
        if num %a==0 and num%b==0:
            return num


# TEST CASES
print(find_lcm(12, 18))  # Expected: 36
print(find_lcm(15, 25))  # Expected: 75
print(find_lcm(7, 13))   # Expected: 91
print(find_lcm(4, 6))    # Expected: 12