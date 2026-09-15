# Return the longest word that appears most frequently.
def longest_word_frequency(text):
    length=0
    result=None
    seen={}
    most=0
    text=text.split()
    for word in text:
        if word not in seen:
            seen[word]=1
        else:
            seen[word]+=1
        # if len(word)>length:
        #     length=len(word)
        #     result=word       
        
    for key , value in seen.items():
        if value >most:
            most=value
        # if value==most:
        # if len(key)>length:
        #     length=len(key)
        #     result=key
    for key , value in seen.items():
        if value==most :
            if len(key)>length:
                length=len(key)
                result=key

    return result
  



    # return result


print(longest_word_frequency("cat dog cat bird"))
# expected: "cat"

print(longest_word_frequency("apple apple banana banana"))
# expected: "banana"

print(longest_word_frequency("hi hello hi hello"))
# expected: "hello"

print(longest_word_frequency(""))
# expected: None