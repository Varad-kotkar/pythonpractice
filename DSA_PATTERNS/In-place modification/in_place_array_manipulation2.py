# Pattern: In-place Array Manipulation
# Filename: in_place_array_manipulation.py

def move_zeros(nums):
    write=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[write]=nums[i]
            write+=1
    while write <len(nums):
        nums[write]=0
        write+=1
    return nums




# Test cases
nums1 = [0, 1, 0, 3, 12]
result1 = move_zeros(nums1)
print(result1)  # Expected: [1, 3, 12, 0, 0]
print(nums1)    # Expected: [1, 3, 12, 0, 0]

nums2 = [0, 0, 0]
print(move_zeros(nums2))  # Expected: [0, 0, 0]

nums3 = [4, 2, 1]
print(move_zeros(nums3))  # Expected: [4, 2, 1]

nums4 = []
print(move_zeros(nums4))  # Expected: []
