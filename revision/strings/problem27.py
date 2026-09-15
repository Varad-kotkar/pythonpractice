# Return a dictionary containing how many times each character appears.
def character_frequency(text):
    seen={}
    for i in text:
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    return seen



print(character_frequency("hello"))
# expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(character_frequency("banana"))
# expected: {'b': 1, 'a': 3, 'n': 2}

print(character_frequency("aabbcc"))
# expected: {'a': 2, 'b': 2, 'c': 2}

print(character_frequency(""))
# expected: {}