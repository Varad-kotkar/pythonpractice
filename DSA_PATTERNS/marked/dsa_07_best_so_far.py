
"""
DSA Pattern: Best-So-Far
Problem 7: Maximum Difference

Find the largest nums[j] - nums[i] where j > i.
The second value must occur after the first.
Return None if fewer than two elements exist.

Examples:
[7, 1, 5, 3, 6, 4] -> 5
[9, 7, 4, 2]       -> -2
[2, 8, 1, 10]      -> 9
[5]                -> None
[]                 -> None

Requirements:
- No sorting, max(), or min()
- O(n) time and O(1) extra space
- Do not modify the input list
"""

def maximum_difference(nums):
    if len(nums)<2:
        return None
# wrong 
    # i=0
    # j=1
    # maximum=nums[j]-nums[i]
    # while j<=len(nums)-1:
    #     if (nums[j]-nums[i]) >maximum:
    #         maximum=nums[j]-nums[i]
    #     i+=1
    #     j+=1
    # return maximum

# brute force approch 
    # maximum=None
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if maximum is None or nums[j]-nums[i] > maximum :
    #             maximum=nums[j]-nums[i]
    # return maximum

# best do far
    smallest_earlier=nums[0]
    maximum=None
    for i in range(1,len(nums)):
        # if nums[i]<smallest_earlier:
        #     smallest_earlier=nums[i]
        if maximum is None or nums[i]-smallest_earlier >maximum:
            maximum=nums[i]-smallest_earlier
        if nums[i]<smallest_earlier:
            smallest_earlier=nums[i]
    return maximum




   


# TEST CASES
print(maximum_difference([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(maximum_difference([9, 7, 4, 2]))        # Expected: -2
print(maximum_difference([2, 8, 1, 10]))       # Expected: 9
print(maximum_difference([5]))                 # Expected: None
print(maximum_difference([]))                  # Expected: None
print(maximum_difference([4, 3]))              # Expected: -1
