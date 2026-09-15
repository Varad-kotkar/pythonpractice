# Return the longest word. If there is a tie, return the first longest word
def longest_word_in_sentence(text):
    if text == "":
        return None
    text=text.split()
    count=0
    longest=0
    word=''
    for i in text:
        count= len(i)
        if count>longest:
            longest=count
            word=i
    return word

print(longest_word_in_sentence("I love programming"))
# expected: "programming"

print(longest_word_in_sentence("Python is very powerful"))
# expected: "powerful"

print(longest_word_in_sentence("cat dog bird"))
# expected: "cat"

print(longest_word_in_sentence(""))
# expected: None

print(longest_word_in_sentence("hello hello world"))
# expected: "hello"