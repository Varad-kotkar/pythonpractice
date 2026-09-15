'''Return the number that appears the most times.

If there is a tie, return the first one that reaches the highest count.'''

def most_common(numbers):
    seen={}
    result=None
    most=0
    for num in numbers:
        if num not in seen:
            seen[num]=1
        else:
            seen[num]+=1
    for key,value in seen.items():
        if value>most:
            most= value
            result=key
    
    return result    

print(most_common([1, 2, 2, 3, 2, 4]))
# expected: 2

print(most_common([5, 5, 2, 2, 2]))
# expected: 2

print(most_common([1, 2, 3]))
# expected: 1

print(most_common([1, 2, 2, 1]))
# expected: 1

print(most_common([]))
# expected: None