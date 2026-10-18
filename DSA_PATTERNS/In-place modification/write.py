def move_zeros(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1

    return nums
# nums = [3, 3, 4]
# for i in nums:
#     if i == 3:
#         nums.remove(i)

# print(nums)