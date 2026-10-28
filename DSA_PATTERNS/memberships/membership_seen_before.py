"""
DSA Pattern: Membership / Seen-Before
Problem 2: Find the First Repeated Value

PROBLEM:
Return the first value encountered that appears for a second time.
If no value repeats, return None.

EXAMPLES:
[4, 7, 2, 7, 4] -> 7
[1, 2, 3]       -> None
[5, 5, 2]       -> 5
[]              -> None

RULE:
The first repeated value is determined by the order in which
repeats are encountered while scanning from left to right.
"""

def first_repeated(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return None


# TEST CASES
print(first_repeated([4, 7, 2, 7, 4]))  # Expected: 7
print(first_repeated([1, 2, 3]))        # Expected: None
print(first_repeated([5, 5, 2]))        # Expected: 5
print(first_repeated([]))               # Expected: None