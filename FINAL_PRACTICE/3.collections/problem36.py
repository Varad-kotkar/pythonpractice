# Move all 0s to the end, while keeping the order of the other numbers.
def move_zeros(numbers):
    count=0
    result=[]

    for num in numbers:
        if num!=0:
            result.append(num)
        if num ==0:
            count+=1
    for  i in range(count):
        result.append(0)
    return result
    

print(move_zeros([0, 1, 0, 3, 12]))   # expected: [1, 3, 12, 0, 0]
print(move_zeros([1, 2, 3]))          # expected: [1, 2, 3]
print(move_zeros([0, 0, 5]))           # expected: [5, 0, 0]
print(move_zeros([1, 0, 2, 0, 3]))    # expected: [1, 2, 3, 0, 0]
print(move_zeros([]))                 # expected: []