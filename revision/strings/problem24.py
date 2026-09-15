# Return the first character that appears only once.
def first_non_repeating(text):
    seen={}
    for i in text:
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    for key, value in seen.items():
        if value ==1:
            return key

print(first_non_repeating("swiss"))      # expected: "w"
print(first_non_repeating("aabbc"))      # expected: "c"
print(first_non_repeating("aabb"))       # expected: None
print(first_non_repeating("hello"))      # expected: "h"
print(first_non_repeating(""))            # expected: None
print(first_non_repeating("aabbcdde"))   # expected: "c"