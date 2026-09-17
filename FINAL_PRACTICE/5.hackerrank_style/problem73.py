# Given a list of integers, find the length of the longest contiguous subarray with no duplicate values.
def longest_unique(numbers):
    seen={}
    count=0
    longest=0
    start = 0
    for  i in range(len(numbers)):
        if numbers[i] not in seen:
            seen[numbers[i]]=i
            count+=1
        else:
            # start=i+1
            new_start = seen[numbers[i]] + 1
            seen[numbers[i]] = i

            if new_start > start:
                start = new_start
            count = i - start + 1
        if count>longest:
            longest=count
    return longest




print(longest_unique([1, 2, 3, 2, 4, 5]))
# expected: 4

print(longest_unique([1, 2, 3, 4]))
# expected: 4

print(longest_unique([1, 1, 1]))
# expected: 1

print(longest_unique([1, 2, 1, 3, 4]))
# expected: 3

print(longest_unique([]))
# expected: 0

print(longest_unique([5]))
# expected: 1