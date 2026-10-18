# Given a string, find the length of the longest substring containing at most 2 distinct characters.
# def longest_two_distinct(s):
#     letters={set()}
#     count=0
#     longest=0
#     for i in s:
#         if i not in letters:
#             letters.add(i)
#             if len(letters)<2:
#                 count+=1
#             else:
#                 count=1
#         if count>longest:
#             longest=count
#     return count
def longest_two_distinct(s):
    left = 0
    counts = {}
    longest = 0

    for right in range (len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        while len(counts)>2:
            counts[s[left]]-=1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left +=1
            # if right-left+1 >longest:
            #     longest=right-left+1
        longest = max(longest, right - left + 1)
    return longest

        # We'll add the next step here       
    

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
