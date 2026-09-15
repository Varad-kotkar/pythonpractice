# The list contains numbers from 1 to n, with one number missing. 
# Return the missing number.
def first_missing(numbers):
    for num in range(1,len(numbers)+2):
        if num not in numbers:
            return num
print(first_missing([1, 2, 3, 5]))
# expected: 4

print(first_missing([1, 2, 4, 5]))
# expected: 3

print(first_missing([2, 3, 4, 5]))
# expected: 1

print(first_missing([1, 2, 3, 4]))
# expected: 5

print(first_missing([2]))
# expected: 1