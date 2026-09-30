# QUESTION:
# Find both the maximum and minimum element in an array.
#
# IMPORTANT TEST CASES:

def find_max_min(arr):
    if not arr:
        return []
    max=None
    min=None
    for  i in arr:
        if max is None or i >max:
            max=i
        if min is None or i< min:
            min =i
    return [min ,max]


print(find_max_min([3,1,5,2,4]))
# Expected: [1,5]

print(find_max_min([-5,-2,-10,-1]))
# Expected: [-10,-1]

print(find_max_min([7]))
# Expected: [7,7]

print(find_max_min([5,5,5]))
# Expected: [5,5]

print(find_max_min([0,-1,2,0]))
# Expected: [-1,2]

print(find_max_min([]))
# Expected: [] or an appropriate empty-input handling