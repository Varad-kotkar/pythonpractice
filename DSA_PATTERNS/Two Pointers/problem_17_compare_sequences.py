# Problem 17: Compare Two Sequences
# Pattern: Two Pointers
# Difficulty: Medium

def common_values(a, b):
    x=0
    y=0
    result=[]
    while x <len(a) and y<len(b):
        if a[x]>b[y]:
            y+=1
        elif a[x]<b[y] :
            x+=1
        else:
            if not result or result[-1] != a[x]:
                result.append(a[x])
            x+=1
            y+=1
    return result

# Tests
print(common_values([1, 2, 3, 4, 6], [2, 4, 6, 8]))
# Expected: [2, 4, 6]

print(common_values([1, 3, 5], [2, 4, 6]))
# Expected: []

print(common_values([1, 1, 2, 3, 3], [1, 2, 2, 3, 4]))
# Expected: [1, 2, 3]

print(common_values([], [1, 2]))
# Expected: []