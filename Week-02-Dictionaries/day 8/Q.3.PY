'''Implement a program that counts how many times each word appears in this sentence:

apple apple mango banana apple banana

Expected output:

{
    "apple": 3,
    "banana": 2,
    "mango": 1
}'''

words ="apple apple mango banana apple banana"
words=words.lower()
words=words.split()
freq={}
for w in words:
    if w not in freq:
        freq[w]=1
    else:
        freq[w]+=1
# a=freq.values()
for key,values in freq.items():
    if values>1:
        print(key)
