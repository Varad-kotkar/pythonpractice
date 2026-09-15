# Return the first number that appears again while scanning from left to right.
def first_repeated(numbers):
    seen=[]
    for num in numbers:
        if num not in seen:
            seen.append(num)
        else:
            return num


print(first_repeated([1, 2, 3, 2, 4]))     # expected: 2
print(first_repeated([5, 1, 5, 2, 1]))     # expected: 5
print(first_repeated([1, 2, 3, 4]))        # expected: None
print(first_repeated([7, 7, 2]))            # expected: 7
print(first_repeated([]))                   # expected: None