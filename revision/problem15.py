'''Return the first number that is smaller than the number immediately before it.

Examples:

[1, 3, 5, 2, 8] → 2
[10, 8, 9, 12] → 8
[1, 2, 3, 4] → None
[5] → None
[] → None
Think first

You're comparing neighbors:

previous → current

For:

[1, 3, 5, 2, 8]
1 → 3  ✅
3 → 5  ✅
5 → 2  ❌  ← return 2'''
def first_decrease(numbers):
    for i in range(len(numbers)-1):


        if numbers[i]>numbers[i+1]:
            return numbers[i+1]
 
print(first_decrease([1, 2, 3, 4,2]))
print(first_decrease([1, 3, 5, 8]))
# print(is_increasing([1, 2, 2, 4]))
# print(is_increasing([5, 3, 4]))
# print(is_increasing([7]))
# print(is_increasing([]))   