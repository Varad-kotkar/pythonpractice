# Given a list of integers, 
# find the length of the longest contiguous subarray 
# containing only positive numbers.
def longest_positive(numbers):
    if numbers==[]:
        return 0
    count =0
    longest=0
    for num in numbers:
        if num >0:
            count+=1
        else:
            count=0
        if count>longest:
            longest=count
    return longest


print(longest_positive([1, 2, 3, -1, 4, 5]))
# expected: 3

print(longest_positive([1, -2, 3, 4, 5]))
# expected: 3

print(longest_positive([-1, -2]))
# expected: 0

print(longest_positive([1, 2, 3]))
# expected: 3

print(longest_positive([]))
# expected: 0

print(longest_positive([0, 1, 2]))
# expected: