# QUESTION:
# Write a function to reverse each word in a sentence,
# while keeping the word order unchanged.
#
# Example:
# "I love Python" → "I evol nohtyP"


def reverse_each_word(s):
    result=[]
    s=s.split()
    for i in s:
        result.append(i[::-1])
    return " ".join(result)



# TEST CASES
print(reverse_each_word("I love Python"))  # Expected: I evol nohtyP
print(reverse_each_word("Hello World"))    # Expected: olleH dlroW
print(reverse_each_word("Python is easy")) # Expected: nohtyP si ysae
print(reverse_each_word("one"))            # Expected: eno
