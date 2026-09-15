# Return a list containing elements that appear in both lists, without duplicates.
def common_elements(list1, list2):
    result=[]
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)

    return result


print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
# expected: [3, 4]

print(common_elements([1, 2, 2, 3], [2, 2, 4]))
# expected: [2]

print(common_elements([1, 2, 3], [4, 5, 6]))
# expected: []

print(common_elements([], [1, 2]))
# expected: []

print(common_elements([3, 1, 2, 3], [3, 2, 3, 5]))
# expected: [3, 2]