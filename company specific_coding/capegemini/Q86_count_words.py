# QUESTION:
# Write a function to count the number of words in a string.
#
# Example:
# "hello world" → 2
# "I love Python" → 3
# "Python" → 1


def count_words(s):
    s=s.split()
    count=0
    for i in s:
        count+=1
    return count


# TEST CASES
print(count_words("hello world"))   # Expected: 2
print(count_words("I love Python")) # Expected: 3
print(count_words("Python"))        # Expected: 1