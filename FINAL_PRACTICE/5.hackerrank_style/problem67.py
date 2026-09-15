# Return a list where duplicates are removed,
#  but keep the last occurrence of each number.
def remove_duplicates_keep_last(numbers):
    if not numbers:
            return []
    # seen=[]
    # for num in numbers:
    #     if num == numbers[-1]:
    #         continue
    #     elif num not in seen:
    #         seen.append(num)
    # seen.append(numbers[-1])
    # return seen
    result=[]
    for i in range(len(numbers)):
        if numbers[i] not in numbers[i + 1:]:
            result.append(numbers[i])
        else:
            continue

    return result
             

print(remove_duplicates_keep_last([1, 2, 1, 3, 2]))
# expected: [1, 3, 2]

print(remove_duplicates_keep_last([4, 4, 4, 2, 2]))
# expected: [4, 2]

print(remove_duplicates_keep_last([1, 2, 3]))
# expected: [1, 2, 3]

print(remove_duplicates_keep_last([]))
# expected: []