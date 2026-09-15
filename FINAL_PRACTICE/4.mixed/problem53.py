# Return the numbers that appear exactly once, keeping their original order.
def single_occurrences(numbers):
    seen={}
    result=[]
    for num in numbers:
        if num not in seen:
            seen[num]=1
        else:
            seen[num]+=1
    for key ,value in seen.items():
        if value ==1:
            result.append(key)
    return result
print(single_occurrences([1, 2, 2, 3, 4, 4]))
# expected: [1, 3]

print(single_occurrences([5, 5, 5]))
# expected: []

print(single_occurrences([1, 2, 3]))
# expected: [1, 2, 3]

print(single_occurrences([]))
# expected: []