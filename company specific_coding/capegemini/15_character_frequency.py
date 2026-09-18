# QUESTION:
# Write a function to count the frequency of each character in a string.
#
# Example:
# "hello"
# h → 1
# e → 1
# l → 2
# o → 1


def character_frequency(s):
    freq={}
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq


# TEST CASES
print(character_frequency("hello"))
# Expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(character_frequency("aabbc"))
# Expected: {'a': 2, 'b': 2, 'c': 1}

print(character_frequency("python"))
# Expected: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}