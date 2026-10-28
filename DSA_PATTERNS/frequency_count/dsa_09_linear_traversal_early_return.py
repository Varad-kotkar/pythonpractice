# ============================================================
# DSA Problem 9: First Element Greater Than Target
# Pattern: Linear Traversal / Early Return
# Difficulty: Easy
# ============================================================

"""
PROBLEM STATEMENT

Given a list of integers nums and an integer target, return
the FIRST element in the list that is strictly greater than
target.

If no element is greater than target, return None.

Important:
- "First" means the element appearing earliest in the list.
- The list is not necessarily sorted.
- Do not modify the original list.

EXAMPLE 1
Input:
    nums = [3, 8, 2, 10, 6]
    target = 5

Expected Output:
    8

Explanation:
    3 is not greater than 5.
    8 is greater than 5, so it is the first valid element.
    We do not need to consider later elements.

EXAMPLE 2
Input:
    nums = [1, 4, 2, 7]
    target = 4

Expected Output:
    7

Explanation:
    The values 1, 4, and 2 are not strictly greater than 4.
    The first value that is greater is 7.

EXAMPLE 3
Input:
    nums = [2, 3, 4]
    target = 4

Expected Output:
    None

Explanation:
    No element is strictly greater than 4.

EXAMPLE 4
Input:
    nums = [-8, -3, -5, 0]
    target = -4

Expected Output:
    -3

Explanation:
    -8 is not greater than -4.
    -3 is the first element that satisfies the condition.

EXAMPLE 5
Input:
    nums = []
    target = 10

Expected Output:
    None

Explanation:
    The list is empty, so no valid element exists.

REQUIREMENTS

1. Implement the function below.
2. Preserve the original list.
3. Return the first qualifying element, not the largest.
4. Return None if no qualifying element exists.
5. Aim for O(n) time complexity.

FUNCTION SKELETON
"""

def first_greater(nums, target):
    for num in nums:
        if num >target:
            return num
    return None


# ============================================================
# TEST CASES — Run these after implementing the function
# ============================================================

tests = [
    ([3, 8, 2, 10, 6], 5, 8),
    ([1, 4, 2, 7], 4, 7),
    ([2, 3, 4], 4, None),
    ([-8, -3, -5, 0], -4, -3),
    ([], 10, None),
    ([9, 2, 8], 5, 9),
    ([5, 5, 5], 5, None),
]

for nums, target, expected in tests:
    original = nums.copy()
    result = first_greater(nums, target)

    print(
        f"nums={nums}, target={target}, "
        f"result={result}, expected={expected}, "
        f"passed={result == expected and nums == original}"
    )

# Expected: passed=True for every test case.