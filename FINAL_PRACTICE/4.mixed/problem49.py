# Combine both lists into one list, keeping the original order and removing duplicates.
def merge_unique(list1, list2):
    result=[]
    for num in list1:
        if num not in result:
            result.append(num)
    for num in list2:
        if num not in result:
            result.append(num)
    return result

print(merge_unique([1, 2, 3], [3, 4, 5]))
# expected: [1, 2, 3, 4, 5]

print(merge_unique([1, 1, 2], [2, 3, 3]))
# expected: [1, 2, 3]

print(merge_unique([], [1, 2]))
# expected: [1, 2]

print(merge_unique([5, 4], [5, 4, 3]))
# expected: [5, 4, 3]