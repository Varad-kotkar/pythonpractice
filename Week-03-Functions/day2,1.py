def build_frequency(data):
    freq={}
    for i in data :
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq


def most_frequent(data):
    freq = build_frequency(data)
    most_freq=0
    most_frequent_key= 0
    for  key,value in freq.items():
        if value >most_freq:
            most_freq=value 
            most_frequent_key=key
    return most_frequent_key

print(most_frequent(x))