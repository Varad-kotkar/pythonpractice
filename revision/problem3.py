'''Problem 3 — Slightly harder

Now let's combine counting + conditions + functions.

Write:

def count_even(numbers):

It should return how many even numbers are in the list.

Examples:

count_even([1, 2, 3, 4, 6]) → 3
count_even([1, 3, 5]) → 0
count_even([-4, -2, 3]) → 2'''

def count_even(numbers):
    count=0
    for num in numbers:
        if num %2==0:
            count+=1

    return count

print(count_even([1, 2, 3, 4, 6]))
print(count_even([1, 3, 5]))
print(count_even([-4, -2, 3]))
print(count_even([]))
