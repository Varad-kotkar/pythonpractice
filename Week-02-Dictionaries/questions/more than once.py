submissions = [
    "Rahul",
    "Varad",
    "Rahul",
    "Amit",
    "Viraj",
    "Amit",
    "Rahul",
    "Karan"
]
'''Requirement
Print the first student who submitted more than once.'''
freq={}
for i in submissions:
    if i not in freq:
        freq[i]=1
    # elif i in freq:
    else:
        freq[i]+=1
for x in submissions:
    if x in freq GG:
# for key,value in freq.items():
#     if   value> 1:

#         print(key)
#     break