'''A shopping website records purchases.

purchases = ["Mouse","Keyboard","Mouse","Laptop","Monitor","Laptop","Mouse","Keyboard"]
Requirement

Print the second most purchased product.'''


purchases = ["Mouse","Keyboard","Mouse","Laptop","Monitor","Laptop","Mouse","Keyboard"]
freq={}
most_freq= 0
second_most =0

for  item in purchases:

    if item not in freq:
        freq[item]=1
    else:
        freq[item]+=1


for key,values in freq.items():
    if values >most_freq:
        most_freq=values

for key,values in freq.items():
    if values > second_most and values != most_freq:
        second_most = values

for key,values in freq.items():
    if values == second_most:
        print(key)
        
 