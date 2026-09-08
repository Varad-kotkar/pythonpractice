'''Write:

def count_vowels(text):

It should return the number of vowels (a, e, i, o, u) in a string.

Examples:

count_vowels("hello") → 2
count_vowels("python") → 1
count_vowels("AEIOU") → 5'''

def count_vowels(text):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in text:
        if i in vowels:
            count+=1
    return count
print(count_vowels("hello") )
print(count_vowels("python")) 
print(count_vowels("AEIOU"))
print(count_vowels("banana"))