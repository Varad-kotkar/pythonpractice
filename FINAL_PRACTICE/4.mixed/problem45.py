# Move all negative numbers to the beginning while keeping the order of the other numbers.
def move_negatives(numbers):
    result=[]
    for num in numbers:
        if num <0:
            result.append(num)
    for num in numbers:
        if num >0:
            result.append(num)
    return result


print(move_negatives([1, -2, 3, 3,-4, 5]))
# expected: [-2, -4, 1, 3, 5]

print(move_negatives([-1, 2, -3, 4]))
# expected: [-1, -3, 2, 4]

print(move_negatives([1, 2, 3]))
# expected: [1, 2, 3]

print(move_negatives([-1, -2, -3]))
# expected: [-1, -2, -3]

print(move_negatives([]))
# expected: []