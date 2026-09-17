# Given a list of integers, find the first element that is greater than every element before it.
# For the first element, consider it automatically valid.
def first_record_high(numbers):
    # for i in range(len(numbers)-1):
    #     if numbers[i]>numbers[i+1]:
    #         continue
    #     else:
    #         return numbers[i+1]
    if numbers==[]:
        return 0
    highest=numbers[0]
    for num in numbers[1:]:
        if num> highest:
            # highest=num
            return num
    return 0    
    # return highest

        

print(first_record_high([3, 1, 5, 2, 7]))
# expected: 5

print(first_record_high([1, 2, 3, 4]))
# expected: 2

print(first_record_high([5, 4, 3, 2]))
# expected: 0

print(first_record_high([2, 2, 3]))
# expected: 3

print(first_record_high([]))
# expected: 0

print(first_record_high([10]))
# expected: 0