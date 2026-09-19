# QUESTION:
# Write a function to find elements that are present in arr1
# but not present in arr2.
#
# Each element should appear only once in the result.
#
# Example:
# arr1 = [1, 2, 3, 4]
# arr2 = [2, 4, 5]
# → [1, 3]


def array_difference(arr1, arr2):
    result=set()
    seen = set(arr2)
    for i in arr1:
        # if i not in arr2:
        if i not in seen:
            result.add(i)
    return list(result)



# TEST CASES
print(array_difference([1, 2, 3, 4], [2, 4, 5]))  # Expected: [1, 3]
print(array_difference([1, 1, 2, 3], [2]))         # Expected: [1, 3]
print(array_difference([1, 2], [1, 2]))            # Expected: []
print(array_difference([5, 6, 7], []))             # Expected: [5, 6, 7]