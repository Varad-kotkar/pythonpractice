def prefix_sum(nums):
    running_sum=0
    prefix=[]
    for num in nums:
        running_sum+=num
        prefix.append(running_sum)
    return prefix
def prefix(prefix,L,R):
    if prefix==[]:
        return 0
    if L==0:
        return prefix[R]
    
    return prefix[R]-prefix[L-1]

p = prefix_sum([4, 2, 7, 3, 5])
print(prefix(p, 1, 3))

p = prefix_sum([4, 2, 7, 3, 5])
print(prefix(p, 0, 2))