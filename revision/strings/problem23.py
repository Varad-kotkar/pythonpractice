'''Return True if the string reads the same forward and backward.

Examples:

"madam" → True
"racecar" → True
"hello" → False
"a" → True
"" → True
Think first

You already know how to:

loop through characters
build a string
use indexes
compare values

Your task is to figure out how to compare the string with its reverse.'''
def is_palindrome(text):
    word = list(map(str.lower, text))

    for i in range(len(word) // 2):
        if word[i] == word[-i-1] :
            continue
        else:
            return False
    return True



print(is_palindrome("madam" ))
print(is_palindrome("racecar"))
print(is_palindrome("hello" ))
print(is_palindrome("a"))
print(is_palindrome("" ))