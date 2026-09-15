# Return the character with the second-highest frequency.
# If there isn't a second distinct frequency, return None.
def second_most_frequent(text):
    seen={}
    highest_freq_count=0
    sec_freq=0
    freq=None
    for i in text:
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    for value in seen.values():
        if value> highest_freq_count:
            highest_freq_count=value
            
    for key,value in seen.items():
        
        if value> sec_freq and value<highest_freq_count:
            sec_freq=value
            freq=key
        

        

    return freq






print(second_most_frequent("aabbbcc"))   # expected: "a"
print(second_most_frequent("banana"))    # expected: "n"
print(second_most_frequent("aabbcc"))    # expected: "a"
print(second_most_frequent("aaaa"))      # expected: None
print(second_most_frequent(""))          # expected: None
print(second_most_frequent("aabbc"))     # expected: "c"