# Find the length of the longest sequence where numbers increase by exactly 1.
def longest_consecutive(numbers):
    if numbers==[]:
        return 0
    
    count=1
    highest=1
    for i in range(len(numbers)-1):
        if numbers[i+1]-numbers[i]==1:
            count+=1
        else:
            count=1
        if count>highest:
            highest=count
    return highest

print(longest_consecutive([1, 2, 3, 5, 6]))
# expected: 3

print(longest_consecutive([10, 11, 12, 13]))
# expected: 4

print(longest_consecutive([1, 3, 4, 5, 7]))
# expected: 3

print(longest_consecutive([5]))
# expected: 1

print(longest_consecutive([]))
# expected: 0