# Convert a list of lists into one list.
def flatten(numbers):
    result=[]
    for i in numbers:
        for j in i:
            result.append(j)
    return result

print(flatten([[1, 2], [3, 4], [5]]))
# expected: [1, 2, 3, 4, 5]

print(flatten([[1], [2, 3], [4, 5]]))
# expected: [1, 2, 3, 4, 5]

print(flatten([]))
# expected: []

print(flatten([[], [1, 2], []]))
# expected: [1, 2]