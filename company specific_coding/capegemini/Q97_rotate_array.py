# QUESTION:
# Write a function to rotate an array to the right by k positions.
#
# Example:
# [1,2,3,4,5], k = 2
# → [4,5,1,2,3]
#
# [1,2,3,4], k = 1
# → [4,1,2,3]


def rotate_array(arr, k):
    result=[]
    for i in range(len(arr)-k,len(arr)):
        result.append(arr[i])

    for j in range(len(arr)-k):
        result.append(arr[j])
    return result



# TEST CASES
print(rotate_array([1,2,3,4,5], 2))
# Expected: [4,5,1,2,3]

print(rotate_array([1,2,3,4], 1))
# Expected: [4,1,2,3]