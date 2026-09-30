# QUESTION:
# Write a function to move all negative numbers to the left side
# of an array.
#
# The relative order does not need to be preserved.
#
# IMPORTANT:
# Any valid arrangement with all negative numbers on the left
# and all non-negative numbers on the right is accepted.
#
# Examples:
# [1,-2,3,-4,5] → [-2,-4,1,3,5]
# [1,2,3]       → [1,2,3]
# [-1,-2,-3]    → [-1,-2,-3]
#
# TEST CASES:
#
# 1. Mixed positive and negative
# [1,-2,3,-4,5]
#
# 2. All positive
# [1,2,3]
#
# 3. All negative
# [-1,-2,-3]
#
# 4. Contains zero
# [0,-1,2,-3]
#
# 5. Single element
# [-5]
#
# 6. Empty array
# []
#
# 7. Repeated negative numbers
# [-1,2,-1,3,-2]


def move_negatives(arr):
    result=[]
    for i in arr:
        if i<0:
            result.append(i)
    for i in arr:
            # if i not in result:
            if i >= 0:
                result.append(i)
    return result


# TEST CASES
print(move_negatives([1,-2,3,-4,5]))
print(move_negatives([1,2,3]))
print(move_negatives([-1,-2,-3]))
print(move_negatives([0,-1,2,-3]))
print(move_negatives([-5]))
print(move_negatives([]))
print(move_negatives([-1,2,-1,3,-2]))