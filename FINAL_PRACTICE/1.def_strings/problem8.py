def largest_positive(numbers):
    largest_num=0
    for num in numbers:
        if num>largest_num:
            largest_num=num
    if largest_num<=0:
        return None
    else:
        return largest_num
print(largest_positive([4, -2, 9, 3]))
print(largest_positive([-5, -2, -8]))
print(largest_positive([0, 7, 2, -1] ))
print(largest_positive([]))
print(largest_positive([3, 3, -2]))