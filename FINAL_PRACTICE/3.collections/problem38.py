# Return the second-largest distinct number.
def second_largest(numbers):
    largest=None
    sec_largest=None
    for num in numbers:
        if largest is None or num>largest:
            largest=num
    for num in numbers:

        if num < largest and (sec_largest is None or num > sec_largest):
            sec_largest=num 

    return sec_largest

print(second_largest([10, 5, 20, 15]))  # expected: 15
print(second_largest([4, 4, 2, 1]))    # expected: 2
print(second_largest([-1, -5, -2]))    # expected: -2
print(second_largest([10]))             # expected: None
print(second_largest([]))               # expected: None
print(second_largest([5, 5, 5]))        # expected: None