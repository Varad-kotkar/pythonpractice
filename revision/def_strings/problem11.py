'''def count_occurrences(numbers, target):

Return how many times target appears in numbers.

Examples:

[1, 2, 3, 2, 4, 2], target=2 → 3
[5, 5, 5], target=5 → 3
[1, 2, 3], target=9 → 0
[], target=5 → 0'''
def count_occurrences(numbers, target):
    count=0
    for num in numbers:
        if target==num:
            count+=1
    return count

print(count_occurrences([1, 2, 3, 2, 4, 2], target=2))