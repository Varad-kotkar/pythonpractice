# QUESTION:
# Write a function to check whether two strings are anagrams.
#
# Two strings are anagrams if they contain the same characters
# with the same frequency.
#
# Example:
# "listen", "silent" → True
# "hello", "world" → False


def is_anagram(s1, s2):
    freq1={}
    freq2={}
    for i in s1:
        if i == " ":
            continue
        if i not in freq1:
            freq1[i]=1
        else:
            freq1[i]+=1
    for i in s2:
        if i == " ":
            continue
        if i not in freq2:
            freq2[i]=1
        else:
            freq2[i]+=1
    return freq1==freq2



# TEST CASES
print(is_anagram("listen", "silent"))  # Expected: True
print(is_anagram("hello", "world"))    # Expected: False
print(is_anagram("triangle", "integral")) # Expected: True
print(is_anagram("python", "typhon"))   # Expected: True