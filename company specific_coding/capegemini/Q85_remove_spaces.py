# QUESTION:
# Write a function to remove all spaces from a string.
#
# Example:
# "hello world" → "helloworld"
# "I love Python" → "IlovePython"


def remove_spaces(s):
    result=[]
    for i in s:
        if i ==" ":
            continue
        else:
            result.append(i)
    return "".join(result)

# TEST CASES
print(remove_spaces("hello world"))   # Expected: "helloworld"
print(remove_spaces("I love Python")) # Expected: "IlovePython"
print(remove_spaces("hello"))         # Expected: "hello"