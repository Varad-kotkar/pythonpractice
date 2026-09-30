# QUESTION:
# Write a function to count how many times a given character
# appears in a string.
#
# Example:
# "banana", "a" → 3
# "hello", "l" → 2


def count_character(s, char):
    freq={}
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for key , value in freq.items():
        if char==key:
            return value
    return 0

# TEST CASES
print(count_character("banana", "a"))  # Expected: 3
print(count_character("hello", "l"))   # Expected: 2
print(count_character("python", "z"))  # Expected: 0