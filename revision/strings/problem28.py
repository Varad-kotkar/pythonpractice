# Return True if both strings contain the same characters with the same frequencies, regardless of order.
def is_anagram(text1, text2):
    # words1=list(map(str.lower(text1).split(), text1))
    # words2=list(map(str.lower(text2).split(), text2))
    # if words1 in words2:
    #     return True
    words1={}
    words2={}
    for i in text1:
        if i not in words1:
            words1[i]=1
        else:
            words1[i]+=1
    for i in text2:
        if i not in words2:
            words2[i]=1
        else:
            words2[i]+=1

    # if words2==words1:
    #     return True
    # else:
    #     return False
                

    return words1 == words2



print(is_anagram("listen", "silent"))     # True
print(is_anagram("hello", "world"))       # False
print(is_anagram("triangle", "integral")) # True
print(is_anagram("aabb", "abab"))         # True
print(is_anagram("aabb", "aab"))          # False
print(is_anagram("", ""))                 # True