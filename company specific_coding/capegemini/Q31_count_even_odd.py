# QUESTION:
# Write a function to count the number of even and odd
# elements in an array.
#
# Example:
# [1, 2, 3, 4, 5] → (2, 3)


def count_even_odd(arr):
    odd=0
    even=0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd


# TEST CASES
print(count_even_odd([1, 2, 3, 4, 5]))  # Expected: (2, 3)
print(count_even_odd([2, 4, 6]))        # Expected: (3, 0)
print(count_even_odd([1, 3, 5]))        # Expected: (0, 3)
print(count_even_odd([]))               # Expected: (0, 0)