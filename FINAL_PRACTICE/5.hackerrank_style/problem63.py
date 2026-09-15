# Remove repeated values only when they are directly next to each other.
def remove_consecutive_duplicates(numbers):
    if not numbers:
        return []
    result=[]
    result.append(numbers[0])
    for  i in range(len(numbers)-1):
        if numbers[i]==numbers[i+1] :
            continue
        else:
            result.append(numbers[i+1])
 
    return result    

print(remove_consecutive_duplicates([1, 1, 2, 2, 3, 3]))
# expected: [1, 2, 3]

print(remove_consecutive_duplicates([1, 2, 1, 2]))
# expected: [1, 2, 1, 2]

print(remove_consecutive_duplicates([5, 5, 5, 2, 2]))
# expected: [5, 2]

print(remove_consecutive_duplicates([1]))
# expected: [1]

print(remove_consecutive_duplicates([]))
# expected: []