# QUESTION:
# Write a function to find the smallest positive number
# that is missing from an array.
#
# Example:
# [3, 4, -1, 1] → 2
#
# Example:
# [1, 2, 0] → 3


def missing_positive(arr):
    for i in range(1,len(arr)+2):
        if i not in arr:
            return i
        

# TEST CASES
print(missing_positive([3, 4, -1, 1]))  # Expected: 2
print(missing_positive([1, 2, 0]))      # Expected: 3
print(missing_positive([7, 8, 9, 11]))  # Expected: 1
print(missing_positive([1, 2, 3]))      # Expected: 4