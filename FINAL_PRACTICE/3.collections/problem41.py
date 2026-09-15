# Return pairs of numbers whose sum equals target.
def find_pairs(numbers, target):
    result=[]
    # for i in range(len(numbers)//2):
    #     # if numbers[i]+ numbers[-i]==target:
    #     #     result.append([numbers[i],numbers[-i]])
    #     # diff=target-numbers[i]
    #     if target-numbers[i]  in numbers :
    #         if[numbers[i],target-numbers[i]] not in result:
    #             result.append([numbers[i],target-numbers[i]])

    # # for num in numbers:
    # #     other = target - num

    # #     if other in numbers :
    # #         if num and other not in result:
    # #             result.append([(num, other)])


    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                if [numbers[i],numbers[j]] not in result:
                    result.append([numbers[i],numbers[j]])
    
    return result


print(find_pairs([1, 2, 3, 4, 5], 6))
# expected: [(1, 5), (2, 4)]

print(find_pairs([2, 4, 6, 8], 10))
# expected: [(2, 8), (4, 6)]

print(find_pairs([1, 1, 2, 3], 4))
# expected: [(1, 3)]

print(find_pairs([1, 2, 3], 10))
# expected: []

print(find_pairs([], 5))
# expected: []