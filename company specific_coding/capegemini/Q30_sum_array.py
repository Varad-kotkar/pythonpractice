# QUESTION:
# Write a function to find the sum of all elements in an array.
#
# Do not use sum().
#
# Example:
# [1, 2, 3, 4, 5] → 15


def array_sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum


# TEST CASES
print(array_sum([1, 2, 3, 4, 5]))  # Expected: 15
print(array_sum([10, 20, 30]))      # Expected: 60
print(array_sum([-1, 2, -3]))       # Expected: -2
print(array_sum([]))                # Expected: 0