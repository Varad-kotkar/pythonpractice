#Return the words in reverse order, not the characters.
# def reverse_words(text):
#     sentence=[]
#     words = text.split()
#     for i in words:
#         sentence.append(i)
#     sentence=sentence[:-1]
#     result="".join(sentence)
#     return result
def reverse_words(text):
    words = text.split()
    words = words[::-1]
    result = " ".join(words)
    return result




print(reverse_words("hello world"))          # expected: "world hello"
print(reverse_words("I love Python"))        # expected: "Python love I"
print(reverse_words("one two three four"))  # expected: "four three two one"
print(reverse_words("hello"))                # expected: "hello"
print(reverse_words(""))                     # expected: ""