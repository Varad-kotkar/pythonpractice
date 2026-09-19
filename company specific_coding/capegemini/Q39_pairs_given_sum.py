# QUESTION:
# Write a function to find all unique pairs of elements
# whose sum equals the target.
#
# Example:
# [1, 2, 3, 4, 5], target = 6 → [(1, 5), (2, 4)]
#
# Each pair should appear only once.


def find_pairs(arr, target):
    result=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                # if (arr[i],arr[j]) not in result:
                result.add((arr[i],arr[j]))
    return list(result)




# TEST CASES
print(find_pairs([1, 2, 3, 4, 5], 6))  # Expected: [(1, 5), (2, 4)]
print(find_pairs([2, 4, 3, 3, 5], 6))  # Expected: [(2, 4), (3, 3)]
print(find_pairs([1, 1, 2, 2], 3))     # Expected: [(1, 2)]
print(find_pairs([1, 2, 3], 10))       # Expected: []