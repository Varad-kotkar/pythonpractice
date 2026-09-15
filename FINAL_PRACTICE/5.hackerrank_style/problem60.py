# Return the number that appears more than half of the total list length.
def majority_element(numbers):
    condition= len(numbers)/2
    count={}
    for num in numbers:
        if num not in count:
            count[num]=1
        else:
            count[num]+=1
    for key , value in count.items():
        if value>condition:
            return key

print(majority_element([2, 2, 1, 2, 3]))
# expected: 2

print(majority_element([3, 3, 4, 3, 2, 3, 3]))
# expected: 3

print(majority_element([1, 2, 3]))
# expected: None

print(majority_element([5]))
# expected: 5

print(majority_element([]))
# expected: None