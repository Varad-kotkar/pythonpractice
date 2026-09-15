'''Return a new string containing each character only once, while keeping its first occurrence order.

Examples:

"programming" → "progamin"
"hello"       → "helo"
"aabbcc"      → "abc"
"python"      → "python"
""            → ""
Think first

You already know:

loop through characters
seen
checking if char not in seen
building a result

Tell me your logic in simple words first, then code it.'''
def remove_duplicates(text):
    seen=[]
    for i in text:
        if i not in seen:
            seen.append(i)

    result= "".join(seen)
    return result
    

print(remove_duplicates("programming" ))
print(remove_duplicates("hello" ))
print(remove_duplicates('aabbcc'))
print(remove_duplicates("python"  ))
print(remove_duplicates(""))

