# Return the number of pairs whose sum equals target.
def count_pairs(numbers, target):
    count=0
    seen=[]
    result=[]
    # for i in numbers:
    #     for j in numbers:
    #         if target-i ==j:
    #                count+=1

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                if [numbers[i],numbers[j]] not in result:
                    result.append([numbers[i],numbers[j]])
                    count+=1
    return count
print(count_pairs([1, 2, 3, 4, 5], 6))
# expected: 2

print(count_pairs([1, 1, 2, 3], 4))
# expected: 1

print(count_pairs([2, 4, 6, 8], 10))
# expected: 2

print(count_pairs([1, 2, 3], 10))
# expected: 0

print(count_pairs([], 5))
# expected: 0