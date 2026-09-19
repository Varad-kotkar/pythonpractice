# QUESTION:
# Write a function to find the first element that appears
# exactly once in an array.
#
# Example:
# [4, 5, 1, 2, 1, 4] → 5
#
# Return None if every element is repeated.


def first_non_repeating(arr):
    freq={}
    result=None
    for i in arr:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1

    for key,value in freq.items():
        if value==1: 
            return key  
   


# TEST CASES
print(first_non_repeating([4, 5, 1, 2, 1, 4]))  # Expected: 5
print(first_non_repeating([1, 2, 2, 1, 3]))      # Expected: 3
print(first_non_repeating([1, 1, 2, 2]))         # Expected: None
print(first_non_repeating([7, 7, 8, 9]))         # Expected: 8