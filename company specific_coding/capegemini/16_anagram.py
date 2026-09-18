# QUESTION:
# Write a function to check whether two strings are Anagrams.
#
# Two strings are anagrams if they contain the same characters
# with the same frequency, but possibly in a different order.
#
# Example:
# "listen" and "silent" → True
# "hello" and "world" → False


def is_anagram(s1, s2):
    freq1={}
    freq2={}
    for i in s1:
        if i not in freq1:
            freq1[i]=1

        else:
            freq1[i]+=1

    for j in s2:
        if j not in freq2:
            freq2[j]=1
        else:
            freq2[j]+=1

    return  freq2==freq1





# TEST CASES
print(is_anagram("listen", "silent"))   # Expected: True
print(is_anagram("hello", "world"))     # Expected: False
print(is_anagram("triangle", "integral")) # Expected: True
print(is_anagram("abc", "abb"))          # Expected: False