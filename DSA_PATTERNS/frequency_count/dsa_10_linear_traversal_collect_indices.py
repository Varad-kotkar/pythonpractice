"""
DSA Problem 10 — Collect Indices Greater Than Target

Pattern: Linear Traversal + Collecting Results
Difficulty: Easy

PROBLEM
-------
Given a list of integers nums and an integer target, return a list
containing the INDEX of every element strictly greater than target.

Remember:
- An index is a position starting from 0.
- Return every matching index, not the matching values.
- Keep the indices in their original order.
- Do not modify the input list.
- If no element matches, return an empty list [].

EXAMPLE 1
---------
Input:
nums = [4, 9, 2, 12, 7]
target = 6

Expected output:
[1, 3, 4]

Explanation:
Index 1 contains 9, index 3 contains 12, and index 4 contains 7.
All three values are strictly greater than 6.

EXAMPLE 2
---------
Input:
nums = [1, 2, 3]
target = 3

Expected output:
[]

Explanation:
No element is strictly greater than 3. Equality does not count.

EXAMPLE 3
---------
Input:
nums = [8, 8, 8]
target = 5

Expected output:
[0, 1, 2]

Explanation:
All three positions qualify, even though the values are equal.

REQUIREMENTS
------------
1. Use a function named collect_indices.
2. Return a list of indices.
3. Handle an empty input list.
4. Do not use list.index() to solve the problem.
5. Try to solve it independently before optimizing anything.

FUNCTION SKELETON
-----------------"""
def collect_indices(nums, target):
    # freq={}
    result=[]
    for i in range(len(nums)):
        # if nums[i] not in freq:
            # freq[i]=nums[i]
        if nums[i]>target:
            result.append(i)
        # else:
        #     freq[num]+=1
    # for key ,values in freq.items():
    #     if values >target:
    #         result.append(key)
    # return result
    return result


# TEST CASES
# ----------
# Test 1
assert collect_indices([4, 9, 2, 12, 7], 6) == [1, 3, 4]

# Test 2: No matching elements
assert collect_indices([1, 2, 3], 3) == []

# Test 3: Every element matches
assert collect_indices([8, 8, 8], 5) == [0, 1, 2]

# Test 4: Empty list
assert collect_indices([], 4) == []

# Test 5: Negative numbers
assert collect_indices([-5, -1, -8, 0], -3) == [1, 3]

# Test 6: Only one match
assert collect_indices([2, 4, 6, 8], 6) == [3]

# Test 7: Values equal to target must be excluded
assert collect_indices([5, 5, 6, 5], 5) == [2]

print("All test cases passed!")