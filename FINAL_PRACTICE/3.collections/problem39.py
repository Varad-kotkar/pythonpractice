# Return a list of numbers that appear more than once, without repeating them in the result.
def find_duplicates(numbers):
    seen={}
    result=[]
    for num in numbers:
        if num not in seen:
            seen[num]=1
        else:
            seen[num]+=1
    for key,value in seen.items():
        if value>1:
            result.append(key)
    return result



print(find_duplicates([1, 2, 2, 3, 1, 4]))
# expected: [2, 1]

print(find_duplicates([5, 5, 5]))
# expected: [5]

print(find_duplicates([1, 2, 3]))
# expected: []

print(find_duplicates([]))
# expected: []

print(find_duplicates([1, 1, 2, 2, 3, 3]))
# expected: [1, 2, 3]