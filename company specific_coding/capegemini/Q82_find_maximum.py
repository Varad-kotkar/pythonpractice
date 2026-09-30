# QUESTION:
# Write a function to find the largest element in an array.
#
# Example:
# [3,7,2,9,4] → 9
# [-5,-2,-10] → -2


def find_maximum(arr):
    largest=None
    for i in arr:
        if largest is None or i >largest:
            largest=i
    return largest


# TEST CASES
print(find_maximum([3,7,2,9,4]))   # Expected: 9
print(find_maximum([-5,-2,-10]))    # Expected: -2