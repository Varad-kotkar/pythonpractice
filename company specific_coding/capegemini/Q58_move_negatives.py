# QUESTION:
# Write a function to move all negative numbers to the beginning
# of an array.
#
# Keep the relative order of the elements.
#
# Example:
# [1, -2, 3, -4, 5] → [-2, -4, 1, 3, 5]


def move_negatives(arr):
    result=[]
    for i in arr:
        if i<0:
            result.append(i)
    for j in arr:        
        if j not in result:
            result.append(j)
    return result
#or

    negative = []
    positive = []

    for i in arr:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)

    return negative + positive


# TEST CASES
print(move_negatives([1, -2, 3, -4, 5]))  # Expected: [-2, -4, 1, 3, 5]
print(move_negatives([-1, 2, -3, 4]))     # Expected: [-1, -3, 2, 4]
print(move_negatives([1, 2, 3]))          # Expected: [1, 2, 3]
print(move_negatives([-1, -2]))            # Expected: [-1, -2]