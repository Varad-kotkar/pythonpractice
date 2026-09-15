# Move the last k elements to the beginning.
def rotate_right(numbers, k):
    if numbers == []:
            return []
    # if k >len(numbers):
    k = k % len(numbers)
    result=[]
    # for i in range(1,k+1):
    #     result.append(numbers[-i])
    # for num in numbers:
    #         result.append(num)   
    # while k!=0:
    #     result.append(numbers[-k])
    #     k-=1
    # k=k
    # result.append(numbers[-k:])
    # for i in range((len(numbers)-k)):
    #     result.append(numbers[i])

    result=numbers[-k:]+numbers[:-k]
    return result



print(rotate_right([1, 2, 3, 4, 5], 2))
# expected: [4, 5, 1, 2, 3]

print(rotate_right([1, 2, 3], 1))
# expected: [3, 1, 2]

print(rotate_right([1, 2, 3, 4], 4))
# expected: [1, 2, 3, 4]

print(rotate_right([1, 2, 3], 5))
# expected: [2, 3, 1]

print(rotate_right([], 2))
# expected: []