'''words = [
    "apple",
    "banana",
    "apple",
    "mango",
    "banana",
    "kiwi",
    "orange",
    "kiwi"
]
Requirement

Print the first unique word.'''

words = [
    "apple",
    "banana",
    "apple",
    "mango",
    "banana",
    "kiwi",
    "orange",
    "kiwi"]

unique=[]
freq={}
for i in words:
    if i not in freq :
        freq[i]=1
    else:
        freq[i]+=1
for key,value in freq.items():
    if value==1:
        unique.append(key)
        break

print(unique)