# Return the number of consecutive equal values in the longest run.
def longest_run(numbers):
    if not numbers:
        return 0
    count=1
    longest=1
    for i in range(len(numbers)-1):
        if numbers[i]==numbers[i+1]:
            count+=1
        else:
            count=1
        if count>longest:
            longest=count
    return longest

print(longest_run([1, 1, 2, 2, 2, 3]))
# expected: 3

print(longest_run([5, 5, 5, 1, 1]))
# expected: 3

print(longest_run([1, 2, 3, 4]))
# expected: 1

print(longest_run([7]))
# expected: 1

print(longest_run([]))
# expected: 0