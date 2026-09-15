# Return the string after removing all vowels.
def remove_vowels(text):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    words=[]

    for i in text:
        if i in vowels:
            continue
        else:
            words.append(i)
    return ''.join(words)


print(remove_vowels("hello"))        # expected: "hll"
print(remove_vowels("programming"))  # expected: "prgrmmng"
print(remove_vowels("AEIOU"))        # expected: ""
print(remove_vowels("Python"))       # expected: "Pythn"
print(remove_vowels("hello world"))  # expected: "hll wrld"
print(remove_vowels(""))             # expected: ""