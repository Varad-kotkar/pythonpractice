"""
DSA — Problem 8: Count Frequency of Elements

Pattern: Frequency Counting
Difficulty: Easy → Developing

PROBLEM

Given a list of integers nums, return a dictionary containing
each distinct number and the number of times it appears.

The dictionary keys must be the distinct numbers from nums.
The corresponding values must be their frequencies.

EXAMPLES

Input:
[2, 3, 2, 5, 3, 2]

Expected output:
{2: 3, 3: 2, 5: 1}

Explanation:
2 appears 3 times, 3 appears 2 times, and 5 appears once.


Input:
[7, 7, 7]

Expected output:
{7: 3}

Explanation:
7 appears 3 times.


Input:
[4, 1, 4, 1]

Expected output:
{4: 2, 1: 2}

Explanation:
Both 4 and 1 appear twice.


Input:
[9]

Expected output:
{9: 1}

Explanation:
The only element appears once.


Input:
[]

Expected output:
{}

Explanation:
An empty list contains no elements to count.


REQUIREMENTS

- Do not use collections.Counter.
- Use a dictionary to store frequencies.
- Aim for O(n) time complexity.
- Do not modify the original list.


FUNCTION

def count_frequency(nums):
    # Write your solution here
    pass


TEST CASES

print(count_frequency([2, 3, 2, 5, 3, 2]))
# Expected: {2: 3, 3: 2, 5: 1}

print(count_frequency([7, 7, 7]))
# Expected: {7: 3}

print(count_frequency([4, 1, 4, 1]))
# Expected: {4: 2, 1: 2}

print(count_frequency([9]))
# Expected: {9: 1}

print(count_frequency([]))
# Expected: {}

print(count_frequency([1, 2, 3]))
# Expected: {1: 1, 2: 1, 3: 1}
"""

def count_frequency(nums):
    freq={}
    for i in nums:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq

# TEST CASES
print(count_frequency([2, 3, 2, 5, 3, 2]))  # Expected: {2: 3, 3: 2, 5: 1}
print(count_frequency([7, 7, 7]))            # Expected: {7: 3}
print(count_frequency([4, 1, 4, 1]))          # Expected: {4: 2, 1: 2}
print(count_frequency([9]))                   # Expected: {9: 1}
print(count_frequency([]))                    # Expected: {}
print(count_frequency([1, 2, 3]))             # Expected: {1: 1, 2: 1, 3: 1}