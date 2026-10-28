word=input("neter the word: ")
freq={}
for char in word :
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1

print(freq)