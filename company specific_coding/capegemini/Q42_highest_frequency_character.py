# QUESTION:
# Write a function to find the character that appears
# most frequently in a string.
#
# If there is a tie, return the character that appears first.
#
# Ignore spaces.
#
# Example:
# "banana" → "a"


def highest_frequency_char(s):
    freq={}
    most_freq=0
    char=None
    for i in s:
        if i == " ":
            continue
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1

    for key,value in freq.items():
        if value>most_freq:
            most_freq=value
            char=key
    return char

        



# TEST CASES
print(highest_frequency_char("banana"))      # Expected: a
print(highest_frequency_char("hello"))       # Expected: l
print(highest_frequency_char("aabbcc"))      # Expected: a
print(highest_frequency_char("python"))      # Expected: p