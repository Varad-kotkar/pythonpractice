# QUESTION:
# Write a function to reverse the order of words in a string.
#
# Example:
# "I love Python" → "Python love I"


def reverse_words(s):
    words = s.split()
    words = words[::-1]
    result = " ".join(words)
    return result



# TEST CASES
print(reverse_words("I love Python"))       # Expected: Python love I
print(reverse_words("Hello World"))         # Expected: World Hello
print(reverse_words("Python is easy"))      # Expected: easy is Python
print(reverse_words("one"))                 # Expected: one