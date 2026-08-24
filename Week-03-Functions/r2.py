def largest(a, b, c):
    if a>b and a>c :
        return a
    elif b>c:
        return b
    else:
        return c

print(largest(10, 20, 30))