def sum_positive(numbers):
    total=0
    for num in numbers:
        if num>0:
            total+=num
    return total

print(sum_positive([1, -2, 3, 0, 5]))
print(sum_positive([-1, -5, 0]))
print(sum_positive([4, 2, 8]))
print(sum_positive([]))
    
