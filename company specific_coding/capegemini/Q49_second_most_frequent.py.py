# QUESTION:
# Write a function to find the second most frequent element
# in an array.
#
# The element must have a different frequency from the most
# frequent element.
#
# If there is no second distinct frequency, return None.
#
# Example:
# [1, 1, 1, 2, 2, 3] → 2


def second_most_frequent(arr):
    freq={}
    most_freq=0
    sec_freq=0
    result=None
    for i in arr:
        # if i == " ":
        #     continue
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1

    for key,value in freq.items():
        if value>most_freq:
            # sec_freq=most_freq
            most_freq=value
    for key,value in freq.items():
        if value>sec_freq and value<most_freq:
            sec_freq=value
            result=key
            
    return result



# TEST CASES
print(second_most_frequent([1, 1, 1, 2, 2, 3]))  # Expected: 2
print(second_most_frequent([5, 5, 4, 4, 4, 3]))  # Expected: 5
print(second_most_frequent([1, 1, 2, 2]))        # Expected: None
print(second_most_frequent([1, 2, 2, 3, 3, 3])) # Expected: 2