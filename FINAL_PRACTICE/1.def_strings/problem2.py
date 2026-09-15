'''Write:

def find_largest(numbers):

It should return the largest number in a list.

Example:

find_largest([4, 8, 2, 10, 6]) → 10
find_largest([-5, -2, -9]) → -2'''

def find_largest(numbers):
    largest_number=numbers[0]
    for num in numbers:
        if num >largest_number:
            largest_number=num
    return largest_number

print(find_largest([4, 8, 2, 10, 6]))
print(find_largest([-5, -2, -9]))