# The list contains numbers from 1 to n, with exactly one number missing. Return the missing number.
def find_missing(numbers):
    n=len(numbers)+1
    for i in range(1,n+1):
        if i not in numbers:
            return i


print(find_missing([1, 2, 4, 5]))      # expected: 3
print(find_missing([1, 3, 4, 5]))      # expected: 2
print(find_missing([2, 3, 4, 5]))      # expected: 1
print(find_missing([1]))               # expected: 2
print(find_missing([1, 2, 3, 5, 6]))   # expected: 4