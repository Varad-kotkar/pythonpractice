# QUESTION:
# An array contains numbers from 1 to n.
# One number is missing and one number is repeated.
# Find both.
#
# Return: [missing, repeated]
#
# IMPORTANT TEST CASES:

def find_missing_repeated(arr):
    freq={}
    repeated=0
    missing=0
    for i in arr:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for key,value in freq.items():
        if value>1:
            repeated=key

    for j in range(1,len(arr)+1):
        if j not in freq:
            missing=j
    return [missing,repeated]
            

            


print(find_missing_repeated([1,2,2,4,5]))
# Expected: [3,2]

print(find_missing_repeated([1,3,3,4]))
# Expected: [2,3]

print(find_missing_repeated([1,1,3]))
# Expected: [2,1]

print(find_missing_repeated([1,2,3,4,4]))
# Expected: [5,4]

print(find_missing_repeated([2,2]))
# Expected: [1,2]

print(find_missing_repeated([1,2,2,3,4,5,6,7,8,9,10,10]))
# Expected: [11,10]