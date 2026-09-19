# QUESTION:
# Write a function to find the first non-repeating character
# in a string.
#
# A non-repeating character appears only once.
#
# Example:
# "aabbcde" → "c"
#
# If there is no non-repeating character, return "".


def first_non_repeating(s):
    seen={}
    

    for i in s:
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    
    for key,value in seen.items():
        if value==1:
            return key 
    return "" ""

        


# TEST CASES
print(first_non_repeating("aabbcde"))  # Expected: c
print(first_non_repeating("aabbcc"))   # Expected: ""
print(first_non_repeating("swiss"))    # Expected: w
print(first_non_repeating("python"))   # Expected: p