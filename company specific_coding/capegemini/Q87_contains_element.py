# QUESTION:
# Write a function to check whether a target element exists
# in an array.
#
# Return True if found, otherwise False.
#
# Example:
# [1,2,3,4], 3 → True
# [1,2,3,4], 7 → False


def contains_element(arr, target):
    return target in arr
       

# TEST CASES
print(contains_element([1,2,3,4], 3))  # Expected: True
print(contains_element([1,2,3,4], 7))  # Expected: False
print(contains_element([], 5))         # Expected: False