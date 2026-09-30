# QUESTION:
# Given an array and a target value, find whether there exists
# a pair of elements whose sum equals the target.
#
# Return True if such a pair exists, otherwise False.
#
# IMPORTANT:
# - Do not use the same element twice.
# - Duplicate values can exist.
#
# Examples:
# [2,7,11,15], target=9 → True
# [1,2,3,4], target=10 → False


def pair_sum(arr, target):
    for i in arr:
        if target-i in arr:
            return True
        else:
            continue
    return False

def pair_sum(arr, target):
    seen = set()

    for i in arr:
        if target-i in seen:
            return True
        seen.add(i)

    return False
    


# TEST CASES

print(pair_sum([2,7,11,15], 9))
# Expected: True

print(pair_sum([1,2,3,4], 10))
# Expected: False

print(pair_sum([3,3], 6))
# Expected: True

print(pair_sum([1,1,1,1], 2))
# Expected: True

print(pair_sum([5], 5))
# Expected: False

print(pair_sum([], 10))
# Expected: False

print(pair_sum([-3,4,2,-1], 1))
# Expected: True

print(pair_sum([0,0], 0))
# Expected: True