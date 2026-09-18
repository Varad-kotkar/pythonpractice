# QUESTION:
# Write a function to remove duplicate characters from a string.
#
# Keep only the first occurrence of each character.
#
# Example:
# "programming" → "progamin"


def remove_duplicates(s):
    result=[]
    for letter  in s:
        if letter not in result:
            result.append(letter)
    return "".join(result)


# TEST CASES
print(remove_duplicates("programming"))  # Expected: progamin
print(remove_duplicates("aabbcc"))       # Expected: abc
print(remove_duplicates("hello"))        # Expected: helo
print(remove_duplicates("python"))       # Expected: python