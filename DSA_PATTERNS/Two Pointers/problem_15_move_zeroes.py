# Problem 15: Move Zeroes to the End
# Pattern: Two Pointers
# Difficulty: Easy–Medium

def move_zeroes(nums):
    write =0
    for read in range(len(nums)):
        if nums[read]!=0:
            nums[write]=nums[read]
            write+=1
    while write<len(nums):
        nums[write]=0
        write+=1

    return nums
            


# Tests
arr1 = [0, 1, 0, 3, 12]
move_zeroes(arr1)
print(arr1)  # Expected: [1, 3, 12, 0, 0]

arr2 = [4, 0, 5, 0, 2]
move_zeroes(arr2)
print(arr2)  # Expected: [4, 5, 2, 0, 0]

arr3 = [1, 2, 3]
move_zeroes(arr3)
print(arr3)  # Expected: [1, 2, 3]

arr4 = [0, 0, 0]
move_zeroes(arr4)
print(arr4)  # Expected: [0, 0, 0]