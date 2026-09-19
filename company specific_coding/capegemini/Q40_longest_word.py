# QUESTION:
# Write a function to find the longest word in a sentence.
#
# If multiple words have the same maximum length,
# return the first one.
#
# Example:
# "I love programming" → "programming"


def longest_word(s):
    longest=0
    word=None
    s=s.split()
    for i in s:
        if len(i)>longest:
            longest=len(i)
            word=i
    return word



# TEST CASES
print(longest_word("I love programming"))    # Expected: programming
print(longest_word("Python is very easy"))   # Expected: Python
print(longest_word("I am a student"))        # Expected: student
print(longest_word("one two six"))           # Expected: one