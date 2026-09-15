# Return elements that appear in all three lists, without duplicates.
def common_three(list1, list2, list3):
    result=[]
    for num in list1:
        if num in list2 and num in list3 and num not in result:
            result.append(num)
    # result=[ num in list2 and num in list3  for num in list1 ]
    return result


print(common_three([1, 2, 3, 4], [2, 3, 5], [0, 2, 3]))
# expected: [2, 3]

print(common_three([1, 2, 2], [2, 3], [2, 4]))
# expected: [2]

print(common_three([1, 2], [3, 4], [1, 2]))
# expected: []

print(common_three([], [1, 2], [1, 2]))
# expected: []