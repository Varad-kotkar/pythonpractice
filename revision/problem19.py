'''Return the longest word in the list.

Examples:

["cat", "elephant", "dog"] → "elephant"
["hi", "hello", "hey"] → "hello"
["a", "bb", "ccc"] → "ccc"
[] → None
Important rule

If two words have the same length, return the first one.

Example:

["cat", "dog", "apple"] → "cat"'''
def longest_word(words):
    longest=0
    longestword=""
    for word in words:
        if len(word)>longest:
            longest=len(word)
            longestword=word
    if not words:
        return None


    return longestword
print(longest_word(["cat", "elephant", "dog"]))
print(longest_word(["hi", "hello", "hey"]))
print(longest_word(["a", "bb", "ccc"]))
print(longest_word([] ))
print(longest_word(["cat", "dog", "ae"] ))
