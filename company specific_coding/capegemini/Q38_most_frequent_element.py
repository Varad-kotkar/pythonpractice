# QUESTION:
# Write a function to find the element that appears
# most frequently in an array.
#
# Example:
# [1, 2, 2, 3, 2, 4] → 2
#
# If there is a tie, return the element that appears first.


def most_frequent(arr):
    seen={}
    most_freq=0
    element=None
    for num in arr:
        if num not in seen:
            seen[num]=1
        else:
            seen[num]+=1
    for key,value in seen.items():
        if value>most_freq:
            most_freq=value
            element=key
    return element

        



# TEST CASES
print(most_frequent([1, 2, 2, 3, 2, 4]))  # Expected: 2
print(most_frequent([5, 1, 5, 2, 1, 1]))  # Expected: 1
print(most_frequent([1, 2, 3]))           # Expected: 1
print(most_frequent([4, 4, 2, 2]))        # Expected: 4