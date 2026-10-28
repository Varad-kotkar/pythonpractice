"""
DSA Problem 12 — Two Sum in a Sorted List
Pattern: Classic Two Pointers
Difficulty: Easy

Problem Statement:
You are given a list of integers sorted in ascending order
and an integer target.

Find two elements at different positions whose sum equals
the target. Return those two values as a list.

If no such pair exists, return an empty list.

Example 1:
Input: nums = [1, 2, 4, 6, 8], target = 10
Expected Output: [2, 8]
Explanation: 2 + 8 = 10.

Example 2:
Input: nums = [1, 3, 5, 7], target = 12
Expected Output: [5, 7]
Explanation: 5 + 7 = 12.

Example 3:
Input: nums = [1, 2, 3, 4], target = 20
Expected Output: []
Explanation: No pair adds up to 20.

Example 4:
Input: nums = [2, 2, 3, 5], target = 4
Expected Output: [2, 2]
Explanation: The two 2s are at different positions.

Example 5:
Input: nums = [], target = 5
Expected Output: []
Explanation: The list is empty.

Requirements:
1. Use the classic two-pointer approach.
2. Do not use nested loops.
3. Do not use a set or dictionary to find the pair.
4. The input list is already sorted.
5. Return the two values, not their indices.
6. Return [] when no valid pair exists.
7. Aim for O(n) time complexity.

Complete the function below.
"""

def two_sum_sorted(nums, target):
    left=0
    right=len(nums)-1
    result=[]
    addition=0
    while left<right:
        addition= nums[left]+nums[right]

        if addition <target:
            left+=1
        if addition> target:
            right-=1
        if addition==target:
            result.append((nums[left],nums[right]))
            break
    return result


# Test cases
print(two_sum_sorted([1, 2, 4, 6, 8], 10))
# Expected: [2, 8]

print(two_sum_sorted([1, 3, 5, 7], 12))
# Expected: [5, 7]

print(two_sum_sorted([1, 2, 3, 4], 20))
# Expected: []

print(two_sum_sorted([2, 2, 3, 5], 4))
# Expected: [2, 2]

print(two_sum_sorted([], 5))
# Expected: []