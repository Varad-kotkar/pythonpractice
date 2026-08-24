def build_frequency(data):
    freq={}
    for i in data :
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq

x=[2,3,2,3,41,24,4,3,1,3,3]
print(build_frequency(x))

def unique_items(freq):
    result = []
    for  key,value in freq.items():
        if value ==1:
            result.append(key)
    return result
        
print(unique_items(build_frequency(x)))
data = build_frequency([2,3,2,3,41,24,4,3,1,3,3])


def most_frequent(data):
    most_freq=0
    most_frequent_key= 0
    for  key,value in data.items():
        if value >most_freq:
            most_freq=value 
            most_frequent_key=key
    return most_frequent_key

print(most_frequent(build_frequency([2,3,2,3,41,24,4,3,1,3,3])))




