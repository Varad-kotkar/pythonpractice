'''nums = [5, 2, 8, 2, 3, 5, 1, 8, 9]
Requirement

Print all numbers that appear exactly once, in sorted order.'''

nums = [5, 2, 8, 2, 3, 5, 1, 8, 9]
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
        # unique.sort()

# unique.sort()
print(unique)