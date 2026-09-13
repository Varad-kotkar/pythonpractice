'''Write:

def first_positive(numbers):

Return the first number greater than 0.

Examples:

[0, -3, 5, 7] → 5
[-2, -1, 4] → 4
[0, -2, 0] → ?
[] → ?'''
def first_positive(numbers):
    for num in numbers:
        if num>0:
            return num

print(first_positive([0, -3, 5, 7]))
print(first_positive([-2, -1, 4] ))
print(first_positive([0, -2, 0]))
print(first_positive([]))