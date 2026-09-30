# QUESTION:
# Write a function to count the number of odd elements in an array.
#
# Example:
# [1,2,3,4,5] → 3
# [2,4,6] → 0


def count_odd_numbers(arr):
    count=0
    for i in arr:
        if i%2!=0:
            count+=1
    return count


# TEST CASES
print(count_odd_numbers([1,2,3,4,5]))  # Expected: 3
print(count_odd_numbers([2,4,6]))      # Expected: 0
print(count_odd_numbers([1,3,5,7]))    # Expected: 4
