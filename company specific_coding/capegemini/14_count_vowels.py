# QUESTION:
# Write a function to count the number of vowels in a given string.
#
# Vowels: a, e, i, o, u
#
# Example:
# "hello" → 2
# "python" → 1


def count_vowels(s):
    s=s.lower()
    Vowels= ['a', 'e', 'i', 'o', 'u']
    count=0
    for i in s:
        if i in Vowels:
            count+=1
    return count
                
                




# TEST CASES
print(count_vowels("hello"))     # Expected: 2
print(count_vowels("python"))    # Expected: 1
print(count_vowels("education")) # Expected: 5
print(count_vowels("sky"))       # Expected: 0