# QUESTION:
# Write a function to find elements common to all three arrays.
#
# Each element should appear only once.
#
# Example:
# [1, 2, 3, 4]
# [2, 3, 5]
# [0, 2, 3]
# → [2, 3]


def common_three_arrays(arr1, arr2, arr3):
    # return list(set(arr1).intersection(set(arr2)).intersection(set(arr3)))
    result=set()
    for i in arr1:
        if i in set(arr2) and i in set(arr3):
            result.add(i)
    return list(result)

# TEST CASES
print(common_three_arrays([1, 2, 3, 4], [2, 3, 5], [0, 2, 3]))
# Expected: [2, 3]

print(common_three_arrays([1, 1, 2, 3], [1, 2], [1, 2, 4]))
# Expected: [1, 2]

print(common_three_arrays([1, 2], [3, 4], [1, 2]))
# Expected: []

print(common_three_arrays([], [1, 2], [1, 2]))
# Expected: []