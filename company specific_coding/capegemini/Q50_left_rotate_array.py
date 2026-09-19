# QUESTION:
# Write a function to rotate an array left by one position.
#
# Example:
# [1, 2, 3, 4, 5] → [2, 3, 4, 5, 1]


def left_rotate(arr):
    if arr==[]:
        return []
    result=[]
    for i in range(len(arr)):
        if i==0:
            continue
        else:
            result.append(arr[i])
    # return arr
    result.append(arr[0])
    return result
    


# TEST CASES
print(left_rotate([1, 2, 3, 4, 5]))  # Expected: [2, 3, 4, 5, 1]
print(left_rotate([10, 20, 30]))     # Expected: [20, 30, 10]
print(left_rotate([1]))              # Expected: [1]
print(left_rotate([]))               # Expected: []