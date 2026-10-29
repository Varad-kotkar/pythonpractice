"""
DSA Pattern: Prefix Sum
Problem 2: Range Sum Queries

Build a prefix sum array and use it to calculate the sum
between indices L and R, inclusive.

Requirements:
- Build the prefix sum array only once.
- Answer queries using the prefix sum array.
- Do not modify the original list.
- Do not use sum() to calculate the range directly.
- Return None for a query on an empty list.

Expected examples:
[2, 4, 6, 8, 10], L=1, R=3 -> 18
[2, 4, 6, 8, 10], L=0, R=2 -> 12
[5, 3, 7, 2],     L=1, R=2 -> 10
[9],               L=0, R=0 -> 9
[],                L=0, R=0 -> None
"""


def build_prefix_sum(nums):
    running_sum=0
    prefix=[]
    for num in nums:
        running_sum+= num
        prefix.append(running_sum)
    return prefix


def range_sum(prefix, L, R):
    if prefix==[]:
        return None
    if L==0:
        return prefix[R]

    return prefix[R]-prefix[L-1]

# TEST CASES

prefix = build_prefix_sum([2, 4, 6, 8, 10])
print(range_sum(prefix, 1, 3))  # Expected: 18
print(range_sum(prefix, 0, 2))  # Expected: 12

prefix = build_prefix_sum([5, 3, 7, 2])
print(range_sum(prefix, 1, 2))  # Expected: 10

prefix = build_prefix_sum([9])
print(range_sum(prefix, 0, 0))  # Expected: 9

prefix = build_prefix_sum([])
print(range_sum(prefix, 0, 0))  # Expected: None