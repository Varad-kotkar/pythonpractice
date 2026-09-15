# Return the difference between the largest and smallest numbers.
def largest_difference(numbers):
    if numbers == []:
        return 0
    largest=None
    for num in numbers:
        if largest == None or num>largest:
            largest= num
    smallest= largest
    for num in numbers:
        if num< smallest:
            smallest=num
    return largest-smallest


print(largest_difference([1, 5, 3, 9, 2]))   # expected: 8
print(largest_difference([10, 20, 30]))       # expected: 20
print(largest_difference([-5, -2, -10]))      # expected: 8
print(largest_difference([7]))                # expected: 0
print(largest_difference([]))                 # expected: 0