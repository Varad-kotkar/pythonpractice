'''Return True if two consecutive numbers are equal, otherwise return False.

Examples:

[1, 2, 3, 3, 5] → True
[1, 2, 3, 4] → False
[5, 5, 2] → True
[1] → False
[] → False'''
def has_adjacent_duplicates(numbers):
    for i in range(len(numbers)-1):


        if numbers[i]==numbers[i+1]:
            return True

    return False
print(has_adjacent_duplicates([1, 2, 3, 3, 5]))
print(has_adjacent_duplicates([1, 2, 3, 4]))
print(has_adjacent_duplicates([5, 5, 2] ))
print(has_adjacent_duplicates([1] ))
print(has_adjacent_duplicates([] ))
