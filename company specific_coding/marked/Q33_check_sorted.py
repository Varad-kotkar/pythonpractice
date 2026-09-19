# QUESTION:
# Write a function to check whether an array is sorted
# in ascending order.
#
# Return True if sorted, otherwise False.
#
# Example:
# [1, 2, 3, 4, 5] → True
# [1, 3, 2, 4] → False


def is_sorted(arr):
    # sorted=set()
    # sorted=[]
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
         
    return True




    #         # sorted.add(arr[i]) or sorted.add(arr[i+1])
    #         sorted.append(arr[i]) 
    # # return sorted
    # return list(sorted)==arr


# TEST CASES
print(is_sorted([1, 2, 3, 4, 5]))  # Expected: True
print(is_sorted([1, 3, 2, 4]))     # Expected: False
print(is_sorted([5, 5, 5]))        # Expected: True
print(is_sorted([]))               # Expected: True