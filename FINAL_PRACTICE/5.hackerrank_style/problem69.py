# Return the length of the longest contiguous subarray whose sum is 0.
def longest_zero_sum(numbers):
    sum = 0
    seen={0:-1,}
    largest=0
    for i in range(len(numbers)):
        sum+= numbers[i]
        if sum not in seen:
            seen[sum]=i
        else:
            if (i - seen[sum])>largest:
                largest=i - seen[sum]

    return largest

print(longest_zero_sum([1, -1]))
# expected: 2

print(longest_zero_sum([1, 2, -3, 3]))
# expected: 3

print(longest_zero_sum([1, -1, 2, -2]))
# expected: 4

print(longest_zero_sum([1, 2, 3]))
# expected: 0

print(longest_zero_sum([]))
# expected: 0

print(longest_zero_sum([0]))
# expected: 1

print(longest_zero_sum([1, -1, 3, 2, -5]))
# expected: 5