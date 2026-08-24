nums = [4, 7, 2, 4, 8, 7, 9, 5]
'''Requirement
Print the first number that never repeats.'''


unique=[]
freq={}
for i in nums:
    if i not in freq :
        freq[i]=1
    else:
        freq[i]+=1
for key,value in freq.items():
    if value==1:
        unique.append(key)

print(unique)