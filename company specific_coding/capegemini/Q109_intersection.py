# QUESTION:
# Given two arrays, return their common elements.
#
# Return each common value only ONCE.
#
# IMPORTANT TEST CASES:

def intersection(arr1, arr2):
    # return list(set(arr1).intersection(set(arr2)))
    # result=[]
    # for i in arr1:
    #     if i in arr2:
    #         result.append(i)
    # return result

    return set(arr1) & set(arr2)


print(intersection([1,2,2,3], [2,2,4]))
# Expected: [2]

print(intersection([1,2,3], [4,5,6]))
# Expected: []

print(intersection([1,2,3], [1,2,3]))
# Expected: [1,2,3]

print(intersection([], [1,2]))
# Expected: []

print(intersection([1,1,1], [1,1]))
# Expected: [1]

print(intersection([-1,0,2], [0,2,3]))
# Expected: [0,2]