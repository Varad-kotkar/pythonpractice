n=input("Enter the word")
vowels='aeiouAEIOU'
count=0
for i in n:
    if i in vowels:
        count+=1

print(count)