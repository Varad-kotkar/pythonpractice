'''Return the number that appears most often.

Examples:

[1, 2, 2, 3, 2, 4] → 2
[5, 5, 2, 2, 2] → 2
[1, 2, 3] → 1
[] → None

If there is a tie, return the number that appears first in the list.

Example:

[1, 2, 2, 1] → 1'''
def most_frequent(numbers):
    seen={}
    highest_count=0
    most_frequent_value=None
    for char in numbers:
        
        if char not in seen:
            seen[char]=1
        else:
            seen[char]+=1
    for key,values in seen.items():
        if  values >highest_count:
            highest_count=values
            most_frequent_value=key

    
      
    return most_frequent_value
print(most_frequent([1, 2, 2, 3, 2, 4]))
print(most_frequent([5, 5, 2, 2, 2]))
print(most_frequent([1, 2, 3]))
print(most_frequent([]))
print(most_frequent([1, 2, 2, 1]))