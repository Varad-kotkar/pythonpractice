# Return a new list with all occurrences of target removed.
def remove_all(numbers, target):
    result=[]
    for num in numbers:
        if num==target:
            continue
        else:
            result.append(num)
    return result

print(remove_all([1, 2, 3, 2, 4, 2], 2))
# expected: [1, 3, 4]

print(remove_all([5, 5, 5], 5))
# expected: []

print(remove_all([1, 2, 3], 4))
# expected: [1, 2, 3]

print(remove_all([], 2))
# expected: []