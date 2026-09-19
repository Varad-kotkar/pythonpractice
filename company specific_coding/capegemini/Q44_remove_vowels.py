# QUESTION:
# Write a function to remove all vowels from a string.
#
# Example:
# "Hello World" → "Hll Wrld"


def remove_vowels(s):
    # Vowels= ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    Vowels="aeiouAEIOU"
    result=[]
    for i in s:
        if i not in Vowels:
            result.append(i)
    return "".join(result)
    


# TEST CASES
print(remove_vowels("Hello World"))  # Expected: Hll Wrld
print(remove_vowels("Python"))       # Expected: Pythn
print(remove_vowels("AEIOU"))        # Expected: 
print(remove_vowels("sky"))          # Expected: sky