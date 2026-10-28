# Problem 16: Remove Duplicates from a Sorted Array
# Pattern: Two Pointers
# Difficulty: Easy–Medium

def remove_duplicates(nums):
    a=0
    b=1
    if nums==[]:
        write=0
    else:
        write=1
    # for i in range(len(nums)):
    while b<len(nums):
        if nums[a]==nums[b]:
            a+=1
            b+=1
            continue
        else:
            nums[write]=nums[b]
            a+=1
            b+=1
            write+=1

    return write
    # write=0
    # for read in range (len(nums)):
    #     if nums[write]!=nums[read]:
    #         nums[write]= nums[read]
    #         write+=1
    # return write




# Tests
arr1 = [1, 2, 3, 4]
k1 = remove_duplicates(arr1)
print(k1, arr1[:k1])  # Expected: 2 [1, 2]

arr2 = [0, 0, 1, 1, 1, 2, 2, 3]
k2 = remove_duplicates(arr2)
print(k2, arr2[:k2])  # Expected: 4 [0, 1, 2, 3]

arr3 = [5, 5, 5]
k3 = remove_duplicates(arr3)
print(k3, arr3[:k3])  # Expected: 1 [5]

arr4 = []
k4 = remove_duplicates(arr4)
print(k4, arr4[:k4])  # Expected: 0 []