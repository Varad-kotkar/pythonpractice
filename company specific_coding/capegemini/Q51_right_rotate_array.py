# QUESTION:
# Write a function to rotate an array right by one position.
#
# Example:
# [1, 2, 3, 4, 5] → [5, 1, 2, 3, 4]


def right_rotate(arr):
    if arr==[]:
        return []
    result=[]
    for i in range(-1,len(arr)-1):
        # if i==0:
        #     continue
        # else:
        result.append(arr[i])
    
    # result.append(arr[])
    return result    


# TEST CASES
print(right_rotate([1, 2, 3, 4, 5]))  # Expected: [5, 1, 2, 3, 4]
print(right_rotate([10, 20, 30]))     # Expected: [30, 10, 20]
print(right_rotate([1]))              # Expected: [1]
print(right_rotate([]))               # Expected: []