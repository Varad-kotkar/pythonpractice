def first_negative(numbers):
    for num in numbers:
        if num<0:
            return num

print(first_negative([4, 8, -3, -7] ))
print(first_negative([1, 2, 3]))
print(first_negative([-5, -2, 7] ))
print(first_negative([0, 4, -1]))
print(first_negative([]))