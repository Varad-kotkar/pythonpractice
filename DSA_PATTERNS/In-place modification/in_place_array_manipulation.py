
# DSA Problem 1: Remove All Occurrences of a Value

def remove_value(nums, target):
    result=[]
    for i in nums:
        if i==target:
            continue
        else:
            result.append(i)
    return result
            


# Test cases
print(remove_value([3, 2, 2, 3], 3))       # Expected: [2, 2]
print(remove_value([1, 2, 3, 4], 5))       # Expected: [1, 2, 3, 4]
print(remove_value([5, 5, 5], 5))          # Expected: []
print(remove_value([], 2))                 # Expected: []
print(remove_value([1, 2, 1, 3, 1], 1))    # Expected: [2, 3]
