"""
DSA Pattern: In-place Array Manipulation
Problem 3: Remove Duplicates from a Sorted Array

PROBLEM:
Given a sorted list of integers, remove duplicate values in place
while preserving the order of unique elements.

Modify the original list; do not create a second result list.
Return k, the number of unique elements.
The first k positions of nums must contain the unique values.

EXAMPLES:
[1, 1, 2, 2, 3] -> k = 3, first k elements: [1, 2, 3]
[1, 1, 1, 1]    -> k = 1, first k elements: [1]
[1, 2, 3, 4]    -> k = 4, first k elements: [1, 2, 3, 4]
[]              -> k = 0, first k elements: []

CONSTRAINTS:
- The list is sorted in non-decreasing order.
- Modify nums in place.
- Use O(1) extra space.
- Preserve the order of unique values.
"""

def remove_duplicates(nums):
    if nums==[]:
        return 0
    write=1
    # count=0
    for i in range(1,len(nums)):
        if nums[i]!=(nums[write - 1]):
            nums[write]=nums[i]
            write+=1
            # count+=1
    return write
        
        


# TEST CASES

nums1 = [1, 1, 2, 2, 3]
k1 = remove_duplicates(nums1)
print(k1)          # Expected: 3
print(nums1[:k1])  # Expected: [1, 2, 3]

nums2 = [1, 1, 1, 1]
k2 = remove_duplicates(nums2)
print(k2)          # Expected: 1
print(nums2[:k2])  # Expected: [1]

nums3 = [1, 2, 3, 4]
k3 = remove_duplicates(nums3)
print(k3)          # Expected: 4
print(nums3[:k3])  # Expected: [1, 2, 3, 4]

nums4 = []
k4 = remove_duplicates(nums4)
print(k4)          # Expected: 0
print(nums4[:k4])  # Expected: []