# Return elements that are present in list1 but not in list2, without duplicates.
def list_difference(list1, list2):
    result=[]
    for item in list1:
        if item not in list2 and item not in result:
            result.append(item)
    return result

print(list_difference([1, 2, 3, 4], [2, 4]))
# expected: [1, 3]

print(list_difference([1, 1, 2, 3], [2]))
# expected: [1, 3]

print(list_difference([1, 2, 3], [1, 2, 3]))
# expected: []

print(list_difference([], [1, 2]))
# expected: []
