# QUESTION:
# Write a function to count the frequency of each element
# in an array.
#
# Example:
# [1, 2, 2, 3, 1, 2] → {1: 2, 2: 3, 3: 1}


def frequency(arr):
    freq={}
    for i in arr:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq


# TEST CASES
print(frequency([1, 2, 2, 3, 1, 2]))  # Expected: {1: 2, 2: 3, 3: 1}
print(frequency([1, 1, 1, 1]))         # Expected: {1: 4}
print(frequency([5, 6, 7]))            # Expected: {5: 1, 6: 1, 7: 1}
print(frequency([]))                   # Expected: {}