# QUESTION:
# Write a function to find all duplicate elements in an array.
#
# Each duplicate element should appear only once in the result.
#
# Example:
# [1, 2, 3, 2, 4, 1, 5] → [2, 1]


def find_duplicates(arr):
    # seen=[]
    duplicate=[]
    # for num in arr:
    #     if num not in seen:
    #         seen.append(num)
    #     else:
    #         if num not in duplicate: 
    #             duplicate.append(num)

    # return duplicate
    seen=set()

    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            duplicate.append(i)
    return duplicate


# TEST CASES
print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))  # Expected: [2, 1]
print(find_duplicates([1, 1, 1, 2, 2]))         # Expected: [1, 2]
print(find_duplicates([1, 2, 3, 4]))            # Expected: []
print(find_duplicates([5, 5, 4, 4, 3]))         # Expected: [5, 4]