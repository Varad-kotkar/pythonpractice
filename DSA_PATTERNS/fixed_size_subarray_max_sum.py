
"""
Problem: Maximum Sum of a Fixed-Size Subarray
Pattern: Fixed-Size Sliding Window
Difficulty: Medium

PROBLEM:
Given a list of integers nums and a positive integer k,
return the maximum sum of any consecutive group of exactly
k elements.

EXAMPLE 1:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The consecutive group [5, 1, 3] has sum 9,
which is the largest sum among all groups of 3 elements.

EXAMPLE 2:
Input: nums = [2, 3, 4, 1, 5], k = 2
Output: 7
Explanation: The group [3, 4] has sum 7.

EXAMPLE 3:
Input: nums = [-4, -2, -7, -1], k = 2
Output: -3
Explanation: The group [-2, -1] has the largest sum, -3.

EXAMPLE 4:
Input: nums = [8], k = 1
Output: 8

REQUIREMENTS:
1. Consider only consecutive elements.
2. Every group must contain exactly k elements.
3. The list contains at least k elements.
4. Do not sort or modify nums.
5. First solve it in your own way. We will optimize later.

FUNCTION:"""
def max_subarray_sum(nums, k):
    # Write your logic here
    pass

# TEST CASES:
print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))  # Expected: 9
print(max_subarray_sum([2, 3, 4, 1, 5], 2))      # Expected: 7
print(max_subarray_sum([-4, -2, -7, -1], 2))     # Expected: -3
print(max_subarray_sum([8], 1))                  # Expected: 8
print(max_subarray_sum([1, 2, 3, 4], 4))         # Expected: 10
print(max_subarray_sum([5, -10, 6, 2], 2))       # Expected: 8

