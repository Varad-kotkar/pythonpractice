# QUESTION:
# Write a function to reverse an array.
#
# Do not use reverse() or [::-1].
#
# Example:
# [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]


def reverse_array(arr):
    result=[]
    for i in range(1,len(arr)+1):
        result.append(arr[-i])
    return result


# TEST CASES
print(reverse_array([1, 2, 3, 4, 5]))  # Expected: [5, 4, 3, 2, 1]
print(reverse_array([10, 20, 30]))     # Expected: [30, 20, 10]
print(reverse_array([1]))              # Expected: [1]
print(reverse_array([]))               # Expected: []