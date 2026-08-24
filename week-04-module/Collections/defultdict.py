from collection import defaultdict
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
d=defaultdict
for fruit in words:
    if fruit not in d :
        d[fruit]=1
    else:
        d[fruit]+=1
