# Given a string, find the length of the longest substring containing at most 2 distinct characters.
def longest_two_distinct(s):
    letters={set()}
    count=0
    longest=0
    for i in s:
        if i not in letters:
            letters.add(i)
            if len(letters)<2:
                count+=1
            else:
                count=1
        if count>longest:
            longest=count
    return count
        
    

print(longest_two_distinct("eceba"))
# expected: 3

print(longest_two_distinct("ccaabbb"))
# expected: 5

print(longest_two_distinct("aaaa"))
# expected: 4

print(longest_two_distinct("abc"))
# expected: 2

print(longest_two_distinct(""))
# expected: 0

print(longest_two_distinct("a"))
# expected: 1
