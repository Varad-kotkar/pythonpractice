"""
DSA Pattern: Membership / Seen-Before
Problem 4: Two Sum — Find Whether a Pair Exists

PROBLEM:
Given a list of integers nums and an integer target,
return True if any two DIFFERENT elements add up to target.
Otherwise, return False.

EXAMPLES:
nums = [2, 7, 11, 15], target = 9  -> True
nums = [1, 2, 3, 4], target = 8    -> False
nums = [3, 3], target = 6          -> True
nums = [5], target = 10            -> False
nums = [], target = 5              -> False

REQUIREMENTS:
- Use a set to remember previously visited numbers.
- Do not use the same element twice.
- Do not modify the input list.
- Aim for O(n) average time complexity.
"""

def pair_exists(nums, target):
    seen=set()
    for i in nums:
        if target-i not in seen:
            seen.add(i)
        else:
            return True
    return False  
    #     if target<i:
    #         if i-target not in nums and i not in seen:
    #             return True
    #         else:
    #             seen.add(i)
    #     elif target>i:
    #         if target-i not in nums and i not in seen:
    #             return True
    #         else :
    #             seen.add(i)
    # return False



# TEST CASES
print(pair_exists([2, 7, 11, 15], 9))  # Expected: True
print(pair_exists([1, 2, 3, 4], 8))    # Expected: False
print(pair_exists([3, 3], 6))          # Expected: True
print(pair_exists([5], 10))            # Expected: False
print(pair_exists([], 5))              # Expected: False
print(pair_exists([1, 4, 6, 8], 10))   # Expected: True
print(pair_exists([4], 8))
print(pair_exists([4, 4], 8))