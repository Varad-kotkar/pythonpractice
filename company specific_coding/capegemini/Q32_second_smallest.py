# QUESTION:
# Write a function to find the second smallest distinct element
# in an array.
#
# Do not use sort().
#
# Example:
# [5, 2, 8, 1, 3] → 2
#
# If there is no second distinct smallest element, return None.


def second_smallest(arr):
    smallest=arr[0]
    sec_smallest=None
    for num in arr:
        if num<smallest:
            sec_smallest=smallest
            smallest= num
        elif (sec_smallest is None  or num<sec_smallest) and num!=smallest:
            sec_smallest=num
    return sec_smallest


# TEST CASES
print(second_smallest([5, 2, 8, 1, 3]))  # Expected: 2
print(second_smallest([10, 5, 8, 2]))    # Expected: 5
print(second_smallest([1, 1, 2, 3]))     # Expected: 2
print(second_smallest([5, 5, 5]))        # Expected: None
print(second_smallest([-5, -2, -10]))    # Expected: -5