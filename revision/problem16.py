'''Return the first character that appears exactly once.

Examples:

"swiss" → "w"
"aabbc" → "c"
"hello" → "h"
"aabb" → None
"" → None'''
def first_unique_char(text):
    seen={}
    for char in text:
        
        if char not in seen:
            seen[char]=1
        else:
            seen[char]+=1
    for key,values in seen.items():
        if values==1:
            return key

print(first_unique_char('swiss'))
print(first_unique_char("aabbc"))
print(first_unique_char('aabb'))
print(first_unique_char(''))
print(first_unique_char('hello'))