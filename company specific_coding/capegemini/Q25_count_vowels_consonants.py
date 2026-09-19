# QUESTION:
# Write a function to count the number of vowels and consonants
# in a given string.
#
# Ignore spaces, numbers, and special characters.
#
# Example:
# "Hello World" → Vowels: 3, Consonants: 7


def count_vowels_consonants(s):
    s=s.lower()
    Vowels= ['a', 'e', 'i', 'o', 'u']
    vowels_count=0
    consonants_count=0
    for i in s:
        if i.isalpha():  #imp
            if i in Vowels:
                vowels_count+=1
            else:
                consonants_count+=1

    return ( vowels_count,consonants_count)



# TEST CASES
print(count_vowels_consonants("Hello World"))  # Expected: (3, 7)
print(count_vowels_consonants("Python"))       # Expected: (1, 5)
print(count_vowels_consonants("aeiou"))         # Expected: (5, 0)
print(count_vowels_consonants("123!@#"))        # Expected: (0, 0)