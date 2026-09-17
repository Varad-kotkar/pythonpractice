# Given a list of integers, find the length of the longest contiguous sequence where the numbers are strictly increasing
def longest_increasing(numbers):
    if numbers==[]:
        return 0
    longest=1
    count=1
    for i in range(len(numbers)-1):
        if numbers[i]<numbers[i+1]:
            count+=1
        else:
            count=1

        if count>longest:
            longest=count
    return longest



print(longest_increasing([1, 2, 5, 3, 4, 6, 2]))
# expected: 3

print(longest_increasing([1, 2, 3, 4]))
# expected: 4

print(longest_increasing([5, 4, 3, 2]))
# expected: 1

print(longest_increasing([1]))
# expected: 1

print(longest_increasing([]))
# expected: 0

print(longest_increasing([1, 3, 2, 4, 5, 6]))
# expected: 4