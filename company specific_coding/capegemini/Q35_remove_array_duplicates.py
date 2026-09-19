# QUESTION:
# Write a function to remove duplicate elements from an array.
#
# Keep only the first occurrence of each element.
#
# Example:
# [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]


def remove_duplicates(arr):
    seen=set()
    result=[]
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


# TEST CASES
print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # Expected: [1, 2, 3, 4]
print(remove_duplicates([1, 1, 1, 2, 2]))     # Expected: [1, 2]
print(remove_duplicates([5, 4, 3]))           # Expected: [5, 4, 3]
print(remove_duplicates([]))                  # Expected: []