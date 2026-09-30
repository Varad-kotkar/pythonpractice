# QUESTION:
# Given an array and a target difference, determine whether
# there exists a pair of elements whose absolute difference
# equals the target.
#
# Do not use the same element twice.
#
# IMPORTANT TEST CASES:

def pair_difference(arr, target):
    seen=set()

    for num in arr:
        if num+target in seen or num-target in seen:
            return True
        seen.add(num)
    return False



print(pair_difference([5,20,3,2,50,80], 78))
# Expected: True

print(pair_difference([5,20,3,2,50,80], 45))
# Expected: True

print(pair_difference([1,2,3,4,5], 10))
# Expected: False

print(pair_difference([3,3], 0))
# Expected: True

print(pair_difference([5], 0))
# Expected: False

print(pair_difference([], 5))
# Expected: False

print(pair_difference([-5,-2,3], 3))
# Expected: True

print(pair_difference([1,1,1], 0))
# Expected: True