'''Return the length of the longest strictly increasing consecutive sequence.

Examples:

[1, 2, 3, 2, 4, 5, 6] → 4

Because:

1,2,3        → length 3
2,4,5,6      → length 4  ← longest

More examples:

[5, 4, 3]          → 1
[1, 2, 3, 4]       → 4
[1, 2, 1, 2, 3]    → 3
[7]                → 1
[]                 → 0'''
def longest_increasing_run(numbers):
    count=1
    highest_count=0
    for i in range(len(numbers)-1):
        if numbers[i]<numbers[i+1]:
            count+= 1
        else:
            count=1
        if count > highest_count:
            highest_count=count
    if len(numbers)==1:
        return 1
    return highest_count

print(longest_increasing_run([5, 4, 3] ))
print(longest_increasing_run([1, 2, 3, 4] ))
print(longest_increasing_run([1, 2, 1, 2, 3]))
print(longest_increasing_run([7] ))
print(longest_increasing_run([]))
