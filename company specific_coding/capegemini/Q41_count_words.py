# QUESTION:
# Write a function to count the number of words in a sentence.
#
# Multiple spaces should be treated as a single separator.
#
# Example:
# "I love Python" → 3


def count_words(s):
    return len(s.split())



# TEST CASES
print(count_words("I love Python"))       # Expected: 3
print(count_words("Hello   World"))       # Expected: 2
print(count_words("Python"))              # Expected: 1
print(count_words(""))                    # Expected: 0