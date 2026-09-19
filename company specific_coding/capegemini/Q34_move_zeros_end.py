# QUESTION:
# Write a function to move all zeros to the end of an array.
#
# Maintain the relative order of the non-zero elements.
#
# Example:
# [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]


def move_zeros(arr):
    count=0
    result=[]
    for i in arr:
        if i==0:
            count+=1
        else:
            result.append(i)

    [result.append(0)for s in range(count)]
    return result




# TEST CASES
print(move_zeros([0, 1, 0, 3, 12]))  # Expected: [1, 3, 12, 0, 0]
print(move_zeros([1, 0, 2, 0, 3]))   # Expected: [1, 2, 3, 0, 0]
print(move_zeros([0, 0, 1]))         # Expected: [1, 0, 0]
print(move_zeros([1, 2, 3]))         # Expected: [1, 2, 3]