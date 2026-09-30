# QUESTION:
# Given two arrays, return all unique elements present
# in either array.
#
# IMPORTANT TEST CASES:

def union(arr1, arr2):
    return list(set(arr1).union(set(arr2)))


print(union([1,2,2,3], [2,3,4]))
# Expected: [1,2,3,4]

print(union([1,2,3], [4,5,6]))
# Expected: [1,2,3,4,5,6]

print(union([1,1,1], [1,1]))
# Expected: [1]

print(union([], [1,2,3]))
# Expected: [1,2,3]

print(union([], []))
# Expected: []

print(union([-1,0,2], [0,2,3]))
# Expected: [-1,0,2,3]

print(union([5,4,3], [3,2,1]))
# Expected: [1,2,3,4,5] OR any order if using a set