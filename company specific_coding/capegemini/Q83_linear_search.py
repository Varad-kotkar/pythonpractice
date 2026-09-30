# QUESTION:
# Write a function to find the index of a target element
# in an array using linear search.
#
# If the target is not present, return -1.
#
# Example:
# [10,20,30,40], 30 → 2
# [10,20,30,40], 50 → -1


def linear_search(arr, target):
    loactor={}
    for i in range(len(arr)):
        if target== arr[i]:
            return i
    return -1

# TEST CASES
print(linear_search([10,20,30,40], 30))  # Expected: 2
print(linear_search([10,20,30,40], 50))  # Expected: -1
print(linear_search([5,8,2,9], 5))       # Expected: 0