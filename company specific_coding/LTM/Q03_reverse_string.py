# QUESTION:
# Write a Python program to reverse a string
# without using slicing [::-1] or built-in
# reversal methods.
#
# Example:
# Input: "hello"
# Output: "olleh"
#
# TEST CASES:
# Input: "python"
# Expected: "nohtyp"
#
# Input: "a"
# Expected: "a"
#jknkjb
# Input: "12345"
# Expected: "54321"

# n= str(input())
# # n=n.split()
# result=[]
# for char in range(len(n),0,-1):
#     result.append(n[char])
# print("".join(result))
n = input()
result = ""

for char in n:
    result = char+result

print(result)