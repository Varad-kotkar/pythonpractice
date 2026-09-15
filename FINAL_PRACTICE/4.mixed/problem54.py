# Return the smallest positive integer (1, 2, 3...) that is not present in the list.
def first_missing_positive(numbers):
    if numbers == []:
        return 1

    # smallest=numbers[0]
    # for num in numbers:
    #     if num<smallest:
    #         smallest=num
    for num in range(1,len(numbers)+2):
        if num not in numbers:
            return num

    # return smallest

print(first_missing_positive([1, 2, 4, 5]))
# expected: 3

print(first_missing_positive([3, 4, -1, 1]))
# expected: 2

print(first_missing_positive([1, 2, 3]))
# expected: 4

print(first_missing_positive([-1, 0, 2, 3]))
# expected: 1

print(first_missing_positive([]))
# expected: 1