# Return the number of vowels in the string.
def count_vowels(text):
    vowels=['a','e','i','o','u']
    count=0
    text=text.lower()
    for i in text:
        if i in vowels:
            count+=1

    return count



print(count_vowels("hello"))          # expected: 2
print(count_vowels("programming"))    # expected: 3
print(count_vowels("AEIOU"))          # expected: 5
print(count_vowels("python"))         # expected: 1
print(count_vowels("rhythm"))         # expected: 0
print(count_vowels(""))               # expected: 0