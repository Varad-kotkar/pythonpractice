'''A teacher records marks.

marks = [95,80,95,70,80,95]

Requirement

Print the least frequent mark.'''

marks = [95,80,95,70,80,95]
most_freq= 0
least_freq={}
least =most_freq

for  std in marks:

    if std not in least_freq:
        least_freq[std]=1
    else:
        least_freq[std]+=1
for key,values in least_freq.items():
    if values >most_freq:
        most_freq=values
        # print(f"Most Frequent Mark :",key)
        # print(f"Frequency",values)
least =most_freq

# for key,values in least_freq.items():
#     if values < most_freq:
#         least = most_freq

#         print(f"least Frequent Mark :",key)
#         print(f"Frequency",values)

for key, values in least_freq.items():
    if values < least:
        least = values
print(key)