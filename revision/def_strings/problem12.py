'''Instead of returning how many times the target appears, return a list containing the indexes where it appears.

Examples:

[10, 20, 10, 30, 10], target=10 → [0, 2, 4]
[5, 5, 2], target=5 → [0, 1]
[1, 2, 3], target=9 → []
[] → []'''
def find_occurrences(numbers, target):
    result=[]
    for index, num in enumerate(numbers):
        if num == target:
            result.append(index)

    return result
print(find_occurrences([10, 20, 10, 30, 10], target=10 ))