'''Problem 4 (Most Asked)

You attempted this before but didn't fully understand it.

Count frequency of every character.

Input

hello

Output

{
'h':1,
'e':1,
'l':2,
'o':1
}'''


word = "i love python i love ai"
frequency={}
word=word.split()
# count=1
for ch in word:
    if  ch not in frequency :
        frequency[ch]=1 
    else:
        frequency[ch]+=1

        # if  ch  in frequency :
        #     frequency[ch]=+=1
print(frequency)