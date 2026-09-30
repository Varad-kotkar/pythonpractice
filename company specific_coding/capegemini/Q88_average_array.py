# QUESTION:
# Write a function to find the average of all elements in an array.
#
# Example:
# [10,20,30] → 20.0
# [2,4,6,8] → 5.0


def average_array(arr):
    total=0
    for i in arr:
        total+=i
    return total/ len(arr)

# TEST CASES
print(average_array([10,20,30]))  # Expected: 20.0
print(average_array([2,4,6,8]))   # Expected: 5.0