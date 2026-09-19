# QUESTION:
# Write a function to find the first element that appears
# more than once while scanning the array from left to right.
#
# Example:
# [5, 3, 4, 3, 5] → 3
#
# Return None if there is no repeated element.


def first_repeated(arr):
    # brute force approch
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return arr[i]

    #  O(n) approch
    seen=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return i

# TEST CASES
print(first_repeated([5, 3, 4, 3, 5]))  # Expected: 3
print(first_repeated([1, 2, 3, 2, 1]))  # Expected: 2
print(first_repeated([1, 2, 3]))        # Expected: None
print(first_repeated([7, 7, 2, 3]))    # Expected: 7