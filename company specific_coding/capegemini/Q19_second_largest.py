# QUESTION:
# Write a function to find the second largest distinct element
# in an array.
#
# Do not use sort() or max().
#
# Example:
# [10, 5, 20, 8, 20] → 10


def second_largest(arr):
    largest=None
    sec_largest=None
    for num in arr:
        if largest is None or  num>largest:
            sec_largest=largest
            largest=num
        elif sec_largest is None or num>sec_largest and num<largest:
            sec_largest=num

    return sec_largest
        


# TEST CASES
print(second_largest([10, 5, 20, 8, 20]))  # Expected: 10
print(second_largest([1, 2, 3, 4]))        # Expected: 3
print(second_largest([20, 20, 10, 5]))     # Expected: 10
print(second_largest([5, 5, 5, 3]))        # Expected: 3