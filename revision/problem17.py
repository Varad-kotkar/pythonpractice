'''Return a new list containing only the numbers that appear exactly once.

Examples:

[1, 2, 2, 3, 4, 4] → [1, 3]
[5, 5, 5] → []
[1, 2, 3] → [1, 2, 3]
[] → []
Think first

You already solved Problem 16 using frequency counting.

So reuse that idea:

Step 1: Count how many times each number appears.

Step 2: Go through the original list again.

Step 3: If its count is 1, add it to the result list.

Important:

Return a new list, not just the count.'''
def unique_numbers(numbers):
    seen={}
    result=[]
    for char in numbers:
        
        if char not in seen:
            seen[char]=1
        else:
            seen[char]+=1
    for key,values in seen.items():
        if values==1:

            result.append(key)
    return result
print(unique_numbers([1, 2, 2, 3, 4, 4]))
print(unique_numbers([5, 5, 5]))
print(unique_numbers([1, 2, 3]))
print(unique_numbers([]))