arr = [12, 45, 7, 89, 23]
largest=None
for num in arr:
    if largest is None or num>largest:
        largest=num
print(largest)