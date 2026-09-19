# QUESTION:
# Write a function to find both the largest and smallest
# elements in an array.
#
# Do not use max() or min().
#
# Example:
# [10, 5, 20, 8] → (20, 5)


def find_largest_smallest(arr):
    largets=None
    smallest=arr[0]
    for num in arr:
        if largets is None or num >largets:
            largets=num
        if num<smallest:
            smallest=num
    return largets,smallest


# TEST CASES
print(find_largest_smallest([10, 5, 20, 8]))  # Expected: (20, 5)
print(find_largest_smallest([3, 7, 2, 9, 1])) # Expected: (9, 1)
print(find_largest_smallest([-5, -2, -10]))   # Expected: (-2, -10)
print(find_largest_smallest([100]))           # Expected: (100, 100)
