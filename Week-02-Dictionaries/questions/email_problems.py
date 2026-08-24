emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com"
]
'''
Requirement:
Q.1
Print every email only once.'''


once= set()
for i in emails:
    if i not in once:
        once.add(i)
        print(i)

'''Q.2 Print the email that appears the most.'''
most_freq=0
freq ={}
for  j in emails:

    if j not in freq:
        freq[j]=1
    else:
        freq[j]+=1
for key,values in freq.items():
    if values > most_freq:
        most_freq=values
        print(key)


'''Q.3  Check if "d@gmail.com" exists.'''
check = input("enter email for check :")
if check in emails:
    print(f"given email",{check}, " exists")
else:
    print(f"given email",{check}, " not exists")