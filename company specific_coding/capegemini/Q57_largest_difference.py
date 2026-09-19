# QUESTION:
# Write a function to find the largest difference between
# two elements in an array.
#
# The larger element must come after the smaller element.
#
# Example:
# [7, 1, 5, 3, 6, 4] → 5
# Because 6 - 1 = 5


def largest_difference(arr):
    diff=0
    larget=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]-arr[i] >diff:
                diff=arr[j]-arr[i]
    return diff


# TEST CASES
print(largest_difference([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(largest_difference([2, 3, 10, 6, 4, 8])) # Expected: 8
print(largest_difference([10, 8, 6, 4]))       # Expected: -2