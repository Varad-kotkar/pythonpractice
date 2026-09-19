# QUESTION:
# Write a function to find the common elements between
# two arrays.
#
# Each common element should appear only once.
#
# Example:
# [1, 2, 3, 4] and [3, 4, 5, 6] → [3, 4]


def array_intersection(arr1, arr2):
    # return list(set(arr1).intersection(set(arr2)))
    result=[]
    for i in arr1:  
        if i in arr2:
            if i not in result:
                result.append(i)
    return result


# TEST CASES
print(array_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Expected: [3, 4]
print(array_intersection([1, 2, 2, 3], [2, 2, 4]))     # Expected: [2]
print(array_intersection([1, 2, 3], [4, 5, 6]))        # Expected: []
print(array_intersection([], [1, 2]))                   # Expected: []