'''A teacher gives marks.

marks = [95,80,95,70,80,95]

Output should be

Most Frequent Mark : 95

Frequency : 3'''

marks = [95,80,95,70,80,95]
freq={}
most_freq=0
least =0
for i in marks:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
for key,values in freq.items():
    if values >most_freq:
        most_freq=values
        print(f"Most Frequent Mark :",key)
        print(f"Frequency",values)
    elif values <=least:
        least=values
        print(f"least Frequent Mark :",key)
        print(f"Frequency",values)
