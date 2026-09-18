# QUESTION:
# Write a function to find the missing number in an array.
#
# The array contains numbers from 1 to n,
# with exactly one number missing.
#
# Do not use sort().
#
# Example:
# [1, 2, 4, 5] → 3


def missing_number(arr):
    for i in range(1,len(arr)+2):
        if i not in arr:
            return i

# o(n) approch 
def missing_number(arr):
    actual_sum=0
    except_sum=0
    for i in arr:
        actual_sum+=i
    except_sum = sum(range(1, len(arr) + 2))

    return except_sum- actual_sum
    


# TEST CASES
print(missing_number([1, 2, 4, 5]))  # Expected: 3
print(missing_number([1, 2, 3, 5]))  # Expected: 4
print(missing_number([2, 3, 4, 5]))  # Expected: 1
print(missing_number([1, 2, 3, 4]))  # Expected: 5
