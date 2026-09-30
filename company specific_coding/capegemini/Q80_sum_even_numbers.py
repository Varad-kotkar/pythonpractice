# QUESTION:
# Write a function to find the sum of all even numbers in an array.
#
# Example:
# [1,2,3,4,5,6] → 12
# [2,4,6] → 12
# [1,3,5] → 0


def sum_even_numbers(arr):
    even=0
    for num in arr:
        if num%2==0:
            even+=num

    return even



# TEST CASES
print(sum_even_numbers([1,2,3,4,5,6]))  # Expected: 12
print(sum_even_numbers([2,4,6]))        # Expected: 12
print(sum_even_numbers([1,3,5]))        # Expected: 0