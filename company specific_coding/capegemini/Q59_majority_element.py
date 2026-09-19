# QUESTION:
# Write a function to find the majority element in an array.
#
# The majority element is the element that appears
# more than n/2 times.
#
# Return None if no majority element exists.
#
# Example:
# [2, 2, 1, 1, 1, 2, 2] → 2


def majority_element(arr):
    freq={}
    for i in arr:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1

    for key,value in freq.items():
        if value>(len(arr)/2): 
            return key    

# TEST CASES
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Expected: 2
print(majority_element([3, 3, 4]))                # Expected: 3
print(majority_element([1, 2, 3]))                # Expected: None
print(majority_element([5, 5, 5, 2]))             # Expected: 5