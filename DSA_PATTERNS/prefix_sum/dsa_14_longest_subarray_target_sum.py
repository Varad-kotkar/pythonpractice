
"""
Problem 14: Longest Subarray with a Target Sum

Return the length of the longest non-empty contiguous subarray
whose sum equals target.

If no matching subarray exists, return 0.
"""

def longest_subarray_target_sum(numbers, target):
    # TODO 1: Initialize the running sum.
    # TODO 2: Remember the first position of each prefix sum.
    # TODO 3: Find earlier prefix sums that create the target.
    # TODO 4: Track the longest matching length.
    pass


# Test cases
print(longest_subarray_target_sum([1, 2, -1, 2, 1], 3))  # Expected: 3
print(longest_subarray_target_sum([1, 1, 1], 2))         # Expected: 2
print(longest_subarray_target_sum([1, -1, 1], 1))        # Expected: 3
print(longest_subarray_target_sum([2, 4, 6], 5))          # Expected: 0
print(longest_subarray_target_sum([], 0))                # Expected: 0
print(longest_subarray_target_sum([0, 0, 0], 0))         # Expected: 3
