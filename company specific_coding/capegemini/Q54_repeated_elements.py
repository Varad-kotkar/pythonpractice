# QUESTION:
# Write a function to find all elements that appear more than once.
#
# Each repeated element should appear only once in the result.
#
# Example:
# [1, 2, 2, 3, 1, 4, 2] → [1, 2]


def repeated_elements(arr):
    seen=set()
    result=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            result.add(i)
    return list(result)


# TEST CASES
print(repeated_elements([1, 2, 2, 3, 1, 4, 2]))  # Expected: [1, 2]
print(repeated_elements([1, 1, 2, 2, 3]))         # Expected: [1, 2]
print(repeated_elements([1, 2, 3]))               # Expected: []
print(repeated_elements([5, 5, 5]))               # Expected: [5]