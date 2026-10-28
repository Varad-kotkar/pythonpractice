"""
Problem: Remove All Occurrences of a Value
Pattern: In-Place Modification — Read/Write Pointers
Difficulty: Easy

Problem Statement:
Given a list of integers nums and an integer target,
remove every occurrence of target while preserving the
relative order of the remaining elements.

Use read and write positions to solve the problem.

Return the resulting list containing only the kept elements.

Example 1:
Input: nums = [3, 2, 3, 4, 2, 5], target = 3
Expected Output: [2, 4, 2, 5]
Explanation: Both occurrences of 3 are removed.

Example 2:
Input: nums = [1, 1, 1], target = 1
Expected Output: []
Explanation: Every element matches the target.

Example 3:
Input: nums = [1, 2, 3], target = 4
Expected Output: [1, 2, 3]
Explanation: No element matches the target.

Requirements:
1. Preserve the order of the remaining elements.
2. Use read and write positions.
3. Do not use remove() or a list comprehension.
4. Return only the kept elements.
5. Keep your intentional comments as revision notes.

Complete the function below.
"""

def remove_all_occurrences(nums, target):
    write =0
    for read in range(len(nums)):
        if nums[read]==target:
            continue
        else:
            nums[write]= nums[read]
            write+=1
    return nums[:write]

# Test cases
print(remove_all_occurrences([3, 2, 3, 4, 2, 5], 3))
# Expected: [2, 4, 2, 5]

print(remove_all_occurrences([1, 1, 1], 1))
# Expected: []

print(remove_all_occurrences([1, 2, 3], 4))
# Expected: [1, 2, 3]

print(remove_all_occurrences([], 2))
# Expected: []

print(remove_all_occurrences([5, 2, 5, 5, 3], 5))
# Expected: [2, 3]