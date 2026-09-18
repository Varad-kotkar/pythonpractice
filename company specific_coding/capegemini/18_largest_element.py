# QUESTION:
# Write a function to find the largest element in an array/list.
#
# Do NOT use max().


def find_largest(arr):
    largest=None
    for num in arr:
        if largest is None or num >largest:
            largest=num
    return largest
    


# TEST CASES
print(find_largest([10, 5, 20, 8]))     # Expected: 20
print(find_largest([3, 7, 2, 9, 1]))    # Expected: 9
print(find_largest([-5, -2, -10]))      # Expected: -2
print(find_largest([100]))              # Expected: 100