# QUESTION:
# Given an array containing only 0, 1 and 2,
# sort the array in ascending order.
#
# IMPORTANT TEST CASES:

def sort_012(arr):
    freq={}
    result=[]
    for i in arr:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    # for key,value in freq.items():
    if 0 in freq:

        for a in range(freq[0]):
            result.append(0)
    if 1 in freq:
        for b in range(freq[1]):
            result.append(1)
    if 2 in freq:
        for c in range(freq[2]):
            result.append(2)
    return result
        
print(sort_012([2,0,1,2,1,0]))
# Expected: [0,0,1,1,2,2]

print(sort_012([0,0,0]))
# Expected: [0,0,0]

print(sort_012([2,2,2]))
# Expected: [2,2,2]

print(sort_012([1,1,1]))
# Expected: [1,1,1]

print(sort_012([2,1,0]))
# Expected: [0,1,2]

print(sort_012([]))
# Expected: []

print(sort_012([0]))
# Expected: [0]

print(sort_012([2,0,2,1,0,1,2]))
# Expected: [0,0,1,1,2,2,2]