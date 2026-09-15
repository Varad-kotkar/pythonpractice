# Find the pair of adjacent numbers that appears most often.
def most_frequent_pair(numbers):
    if not numbers:
        return None
    longest=0
    result=[]
    pairs = {}
    for  i in range(len(numbers)-1):
        if (numbers[i],numbers[i+1])not in pairs:
            pairs[numbers[i],numbers[i+1]]=1
        else:
            pairs[numbers[i],numbers[i+1]]+=1
    for key,value in pairs.items():
        if value>longest:
            longest=value
            result=key
            
    return result  

print(most_frequent_pair([1, 2, 1, 2, 1]))
# expected: (1, 2)

print(most_frequent_pair([3, 4, 3, 4, 3, 5]))
# expected: (3, 4)

print(most_frequent_pair([1, 2, 3, 4]))
# expected: (1, 2)

print(most_frequent_pair([5]))
# expected: None

print(most_frequent_pair([]))
# expected: None