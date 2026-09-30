# QUESTION:
# Write a function to find all the "leaders" in an array.
#
# An element is a leader if it is greater than all elements
# to its right.
#
# The last element is always a leader.
#
# Example:
# [16,17,4,3,5,2] → [17,5,2]
#
# IMPORTANT:
# Return the leaders in their original left-to-right order.


# def find_leaders(arr):
#     if arr ==[]:
#         return []
#     leader=arr[-1]
#     result=[]
#     for i in range(len(arr)-2, -1, -1):
#         if arr[i]>arr[i+1]:
#             leader=arr[i+1]
#         else:
#             result.append(leader)
#             leader=arr[i+1]
#     return result[::-1]
def find_leaders(arr):
    if not arr:
        return []

    leader = arr[-1]
    result = [leader]

    for i in range(len(arr)-2, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            result.append(leader)

    return result[::-1]



# TEST CASES

# 1. Normal case
print(find_leaders([16,17,4,3,5,2]))
# Expected: [17,5,2]

# 2. Strictly increasing
print(find_leaders([1,2,3,4,5]))
# Expected: [5]

# 3. Strictly decreasing
print(find_leaders([5,4,3,2,1]))
# Expected: [5,4,3,2,1]

# 4. All elements equal
print(find_leaders([5,5,5,5]))
# Expected: [5]

# 5. Single element
print(find_leaders([10]))
# Expected: [10]

# 6. Empty array
print(find_leaders([]))
# Expected: []

# 7. Negative numbers
print(find_leaders([-1,-2,-3,-2]))
# Expected: [-1,-2]