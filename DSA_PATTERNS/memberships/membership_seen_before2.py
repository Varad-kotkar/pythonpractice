"""
DSA Pattern: Membership / Seen-Before
Problem 3: Find All Duplicate Values

PROBLEM:
Given a list of integers, return a list containing each value
that appears more than once.

Each duplicate value should appear only once in the output.
Preserve the order in which each value is first identified as a duplicate.

EXAMPLES:
[4, 7, 2, 7, 4, 7] -> [7, 4]
[1, 2, 3]          -> []
[5, 5, 5]          -> [5]
[]                 -> []

REQUIREMENTS:
- Use sets to track values already seen and duplicates already found.
- Do not modify the input list.
- Do not return the same duplicate multiple times.
"""

def find_duplicates(nums):
    seen=set()
    result=[]
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            if i not in result:
                result.append(i)
    return result

# TEST CASES
print(find_duplicates([4, 7, 2, 7, 4, 7]))  # Expected: [7, 4]
print(find_duplicates([1, 2, 3]))           # Expected: []
print(find_duplicates([5, 5, 5]))           # Expected: [5]
print(find_duplicates([]))                  # Expected: []
print(find_duplicates([2, 1, 2, 1, 3, 3])) # Expected: [2, 1, 3]