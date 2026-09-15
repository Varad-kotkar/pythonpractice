# Replace consecutive repeated characters with the character followed by its count.
def compress_string(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(len(text)-1):
        if text[i]==text[i+1]:
            count += 1
        else:
            word=text[i]+str(count)
            count=1
            result.append(word)
    result.append(text[-1] + str(count))
    return ''.join(result)

print(compress_string("aaabbc"))      # expected: "a3b2c1"
print(compress_string("aabbcc"))      # expected: "a2b2c2"
print(compress_string("abcd"))        # expected: "a1b1c1d1"
print(compress_string("aaaa"))        # expected: "a4"
print(compress_string("aabbaa"))      # expected: "a2b2a2"
# print(compress_string(""))            # expected: ""
print(compress_string("a"))            # expected: "a1"