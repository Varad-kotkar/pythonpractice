# QUESTION:
# Write a function to find the duplicate number in an array.
#
# The array contains numbers from 1 to n,
# and exactly one number is repeated.
#
# Example:
# [1, 3, 4, 2, 2] → 2
#
# Return the duplicated number.


def find_duplicate(arr):
    seen=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return i



# TEST CASES
print(find_duplicate([1, 3, 4, 2, 2]))  # Expected: 2
print(find_duplicate([3, 1, 3, 4, 2]))  # Expected: 3
print(find_duplicate([1, 1, 2]))        # Expected: 1
print(find_duplicate([2, 2, 1, 3]))     # Expected: 2