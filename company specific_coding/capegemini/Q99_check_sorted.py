# QUESTION:
# Write a function to check whether an array is sorted
# in non-decreasing (ascending) order.
#
# Return True if sorted, otherwise False.
#
# Examples:
# [1,2,3,4] → True
# [1,3,2,4] → False
# [1,1,2,2,3] → True


def is_sorted(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]<=arr[j]:
            i+=1
            j+=1
        else:
            return False
    return True
# TEST CASES

# 1. Strictly increasing
print(is_sorted([1,2,3,4]))
# Expected: True

# 2. Not sorted
print(is_sorted([1,3,2,4]))
# Expected: False

# 3. Duplicate values
print(is_sorted([1,1,2,2,3]))
# Expected: True

# 4. Descending
print(is_sorted([5,4,3,2,1]))
# Expected: False

# 5. Single element
print(is_sorted([5]))
# Expected: True

# 6. Empty array
print(is_sorted([]))
# Expected: True

# 7. Negative numbers
print(is_sorted([-5,-3,-3,-1,2]))
# Expected: True