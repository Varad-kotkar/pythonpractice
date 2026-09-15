# Return the first number that appears exactly once.
def first_unique(numbers):
    seen={}
    for char in numbers:
        
        if char not in seen:
            seen[char]=1
        else:
            seen[char]+=1
    for key,values in seen.items():
        if values==1:
            return key
print(first_unique([4, 5, 1, 2, 1, 4]))
# expected: 5

print(first_unique([1, 2, 2, 3, 1, 4]))
# expected: 3

print(first_unique([1, 1, 2, 2]))
# expected: None

print(first_unique([7]))
# expected: 7

print(first_unique([]))
# expected: None