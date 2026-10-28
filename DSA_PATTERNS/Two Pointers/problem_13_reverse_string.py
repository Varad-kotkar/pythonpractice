# Problem 13: Reverse a String In-Place
# Pattern: Two Pointers
# Difficulty: Easy

def reverse_string(chars):
    # Initialize your pointers
    left=0
    right=len(chars)-1
    while left<right:
#imp to remember is instead of seprate assignment use a, b = b, a
        chars[left],chars[right]=chars[right] ,chars[left]
        # chars[right]=chars[left]
        left+=1
        right-=1



    return chars


# Tests
print(reverse_string(["h", "e", "l", "l", "o"]))
# Expected: ["o", "l", "l", "e", "h"]

print(reverse_string(["P", "y", "t", "h", "o", "n"]))
# Expected: ["n", "o", "h", "t", "y", "P"]

print(reverse_string(["a"]))
# Expected: ["a"]

print(reverse_string([]))
# Expected: []