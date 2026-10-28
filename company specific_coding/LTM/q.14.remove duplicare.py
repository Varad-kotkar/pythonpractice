n=list(map(int,input("enter arr").split()))
seen=set()
result=[]
for i in n:
    if i not in seen:
        seen.add(i)
        result.append(i)

print(result)