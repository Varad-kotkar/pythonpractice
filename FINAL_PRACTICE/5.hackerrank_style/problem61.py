# Return the length of the longest streak where each number is greater than the previous number
def longest_increasing_streak(numbers):
    if not numbers:
        return 0
    count=1
    longest=0
    for  i in range(len(numbers)-1):
        if numbers[i]<numbers[i+1] :
            count+=1
        else:
            count=1
        if count>longest:
            longest=count
    return longest



print(longest_increasing_streak([1, 2, 3, 2, 4, 5]))
# expected: 3

print(longest_increasing_streak([5, 6, 7, 8]))
# expected: 4

print(longest_increasing_streak([5, 4, 3, 2]))
# expected: 1

print(longest_increasing_streak([1, 3, 2, 4, 5, 6]))
# expected: 4

print(longest_increasing_streak([]))
# expected: 0