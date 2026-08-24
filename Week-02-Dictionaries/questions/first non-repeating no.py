'''Problem
nums = [4, 7, 4, 2, 7, 8, 9]

Requirement:

Print the first non-repeating number.'''
purchases = [4, 7, 4, 2, 7, 8, 9]
freq={}
most_freq= 0
second_most =0

for  item in purchases:

    if item not in freq:
        freq[item]=1
    else:
        freq[item]+=1

# for key,values in freq.items():
#     if values ==1:
#         print(key)
#         break

for i in purchases:
    if i in freq and freq[i]==1:
        print(i)
        break