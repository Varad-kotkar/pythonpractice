# Return the length of the longest contiguous sequence
#  where numbers alternate between increasing and decreasing.
def longest_alternating(numbers):
    if not numbers:
        return 0

    if len(numbers) == 1:
        return 1
    count=1
    longest=1
    direction=[]
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            direction.append("<")
        elif numbers[i] > numbers[i+1]:
            direction.append(">")
        else:
            direction.append("=")
        

    for d in range (len(direction)-1):
        if direction[d] != direction[d+1] and direction[d] != "=" and direction[d+1] != "=":
            count+=1
        
        else:
            count=1
        if count>longest:
            longest=count
    return longest+1
    

print(longest_alternating([1, 2, 3, 4]))
print(longest_alternating([5, 4, 3, 2] ))
print(longest_alternating([1, 3, 2, 4, 3]))
print(longest_alternating([1, 1, 2, 3]))
print(longest_alternating([] ))
print(longest_alternating([7]))
