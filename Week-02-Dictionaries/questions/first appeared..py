'''orders = ["Laptop","Mouse","Laptop","Keyboard","Mouse","Monitor","Monitor","Headphones"]
Requirement
Print all products that were ordered more than once, in the order they first appeared.'''

orders = ["Laptop","Mouse","Laptop","Keyboard","Mouse","Monitor","Monitor","Headphones"]

repeated_orders=[]
freq={}
for i in orders:
    if i not in freq :
        freq[i]=1
    else:
        freq[i]+=1
for key,value in freq.items():
    if value>1:
        # print(key)
#         repeated_orders.append(key)


# for item in repeated_orders:
#     print(item)
# print(len(repeated_orders))


        '''Print each repeated product only when it becomes repeated.'''

for i in orders:
    for j in orders:
        if i==j :
            print(j)
        