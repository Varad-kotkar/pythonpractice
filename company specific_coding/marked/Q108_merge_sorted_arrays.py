# QUESTION:
# Given two sorted arrays, merge them into one sorted array.
#
# The resulting array should contain all elements from both arrays.
#
# IMPORTANT TEST CASES:

# def merge_sorted(arr1, arr2):
#     a=0
#     b=0
#     result=[]
#     while a <=len(arr1) or b<=len(arr2):
#         if arr1[a]<arr2[b]:
#             result.append(arr1[a])
#             a+=1
#         # elif arr1[b]<arr2[a]:
#         else:
#             result.append(arr2[b])
#             b+=1
#     return result

def merge_sorted(arr1, arr2):
    a = 0
    b = 0
    result = []

    while a < len(arr1) and b < len(arr2):
        if arr1[a] < arr2[b]:
            result.append(arr1[a])
            a += 1
        else:
            result.append(arr2[b])
            b += 1

    while a < len(arr1):
        result.append(arr1[a])
        a += 1

    while b < len(arr2):
        result.append(arr2[b])
        b += 1

    return result



print(merge_sorted([1,3,5], [2,4,6]))
# Expected: [1,2,3,4,5,6]

print(merge_sorted([1,2,3], [4,5,6]))
# Expected: [1,2,3,4,5,6]

print(merge_sorted([4,5,6], [1,2,3]))
# Expected: [1,2,3,4,5,6]

print(merge_sorted([], [1,2,3]))
# Expected: [1,2,3]

print(merge_sorted([1,2,3], []))
# Expected: [1,2,3]

print(merge_sorted([], []))
# Expected: []

print(merge_sorted([1,1,3], [1,2,2]))
# Expected: [1,1,1,2,2,3]

print(merge_sorted([-3,-1,2], [-2,0,4]))
# Expected: [-3,-2,-1,0,2,4]