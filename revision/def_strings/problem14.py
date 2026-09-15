'''Return True if every number is greater than the number before it.

Examples:

[1, 2, 3, 4] → True
[1, 3, 5, 8] → True
[1, 2, 2, 4] → False
[5, 3, 4] → False
[7] → True
[] → True
🛑 Think first

You've just learned the neighbor pattern:

numbers[i]
numbers[i + 1]

Here the rule is:

Current number must be less than the next number.

For:

[1, 3, 5, 8]

check:

1 < 3 ✅
3 < 5 ✅
5 < 8 ✅

If any one comparison fails → False.

If the entire loop finishes → True.'''

def is_increasing(numbers):
    for i in range(len(numbers)-1):


        if numbers[i]<numbers[i+1]:
            continue

        else:
            return False   
    return True
print(is_increasing([1, 2, 3, 4]))
print(is_increasing([1, 3, 5, 8]))
print(is_increasing([1, 2, 2, 4]))
print(is_increasing([5, 3, 4]))
print(is_increasing([7]))
print(is_increasing([]))