# Return a new list with duplicates removed, while keeping the first occurrence order.
def remove_duplicates(numbers):
    seen=[]
    for num in numbers:
        if num not in seen:
            seen.append(num)
    return seen
        


print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# expected: [1, 2, 3, 4]

print(remove_duplicates([5, 5, 5]))
# expected: [5]

print(remove_duplicates([1, 2, 3]))
# expected: [1, 2, 3]

print(remove_duplicates([]))
# expected: []

print(remove_duplicates([3, 1, 3, 2, 1]))
# expected: [3, 1, 2]