# QUESTION:
# Write a function to count positive numbers, negative numbers,
# and zeros in an array.
#
# Example:
# [1, -2, 0, 3, -5, 0] → (2, 2, 2)


def count_numbers(arr):
    positive_count=0
    negative_count=0
    zero_count=0
    for i in arr:
        if i==0:
            zero_count+=1
        if i >0:
            positive_count+=1
        if i<0:
            negative_count+=1
    return positive_count,negative_count,zero_count


# TEST CASES
print(count_numbers([1, -2, 0, 3, -5, 0]))
# Expected: (2, 2, 2)

print(count_numbers([1, 2, 3]))
# Expected: (3, 0, 0)

print(count_numbers([-1, -2, 0]))
# Expected: (0, 2, 1)