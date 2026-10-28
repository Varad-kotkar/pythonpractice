# Pattern: In-place Array Manipulation
# Filename: in_place_array_manipulation.py

def remove_value_in_place(nums, target):
    write=0
    for num in range (len(nums)):
        if nums[num]!=target:
            nums[write]=nums[num]
            write+=1
    return write
    del nums[write:]
    return nums


# Test cases
nums1 = [3, 2, 2, 3]
k1 = remove_value_in_place(nums1, 3)
print(k1)              # Expected: 2
print(nums1[:k1])      # Expected: [2, 2]

nums2 = [1, 2, 3, 4]
k2 = remove_value_in_place(nums2, 5)
print(k2)              # Expected: 4
# print(nums2[:k2])      # Expected: [1, 2, 3, 4]

nums3 = [5, 5, 5]
k3 = remove_value_in_place(nums3, 5)
print(k3)              # Expected: 0
# print(nums3[:k3])      # Expected: []

nums4 = []
k4 = remove_value_in_place(nums4, 2)
print(k4)              # Expected: 0
# print(nums4[:k4])      # Expected: []